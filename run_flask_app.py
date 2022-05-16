# encoding=utf8
# flask app 主文件
import click
from loguru import logger
from pathlib import Path
import json
from flask_app import db, app
from flask_app.model import Apis
from utils.models import API

json_path = Path(app.root_path).parent.joinpath(
    "api.json")


@click.command()
@click.option('--drop', is_flag=True, help='重建数据库')  # 设置选项
def init(drop):
    """初始化数据库"""
    if drop:
        db.drop_all()
        logger.info("删除数据库...准备重建..")
    db.create_all()
    logger.success("数据库创建成功")


@click.command()
@logger.catch()
def json2sqlite():
    """将json数据转为sqlite数据库"""
    j = json_path.read_text(encoding="utf8")

    jss = json.loads(j)
    for js in jss:
        api = Apis(
            desc=str(js['desc']),
            url=str(js['url']),
            method=str(js['method']),
            data=str(js['data']),
            header=str(js['header'])
        )
        # print(api.desc)
        try:
            db.session.add(api)
            db.session.commit()
            logger.info(f"{api.desc} 写入成功!")
        except Exception as e:
            db.session.rollback()  # 回滚
            logger.error(f"{api.desc}写入数据库错误:{e}")

    logger.success("json To sqlite 成功!")


@click.command()
@logger.catch()
def sqlite2json():
    """将sqlite数据转为json"""
    apis = Apis.query.all()
    apis_ = []
    for api in apis:
        # print(api.url)
        if api.data is None:
            api.data = ""
        if api.header is None:
            api.header = ""
        data = {
            "desc": api.desc,
            "url": api.url,
            "method": api.method,
            "data": api.data,
            "header": api.header,
        }
        try:
            api = API(**data).handle_API()
            apis_.append(api.dict())
        except:
            pass
    # print(apis_)
    with open(json_path, mode="w", encoding="utf8") as j:
        try:
            json.dump(apis_, j, ensure_ascii=False, sort_keys=False, indent=4)
            logger.success("sqlite->json 成功!")
        except Exception:
            logger.exception("写入到 json 文件错误!")


@click.command()
@click.option('--host', '-h', help='监听地址', default="0.0.0.0")
@click.option('--port', '-p', help='监听端口', default=9090)
def start(host, port):
    """启动 flask app"""
    app.run(host=host, port=port, debug=True)


@click.group()
def cli():
    pass


cli.add_command(init)
cli.add_command(start)
cli.add_command(json2sqlite)
cli.add_command(sqlite2json)

if __name__ == "__main__":
    cli()

# encoding=utf8
# 从 api.js 偷别人家的接口
import pathlib
import json
from pydantic import BaseModel
from typing import Optional, Union

path = pathlib.Path(__file__).parent.resolve()


class API(BaseModel):
    """处理自定义 API 数据"""
    desc: str = "Default"
    url: str = ""
    method: str = "GET"
    header: Optional[Union[str, dict]] = ""
    data: Optional[Union[str, dict]]


def main():
    with open(pathlib.Path(path, "touapi.json"), mode="r", encoding="utf8") as c:
        js = json.load(fp=c)

    apis = []
    for j in js:
        # print(j)
        api = API()
        api.url = j[0]
        api.method = j[3]
        api.desc = j[2]
        api.data = j[4]
        apis.append(api.dict())
    # print(apis)

    with open(pathlib.Path(path, "api_tou.json"), mode="w", encoding="utf8") as cc:
        js = json.dump(obj=apis, fp=cc,  ensure_ascii=False)


if __name__ == "__main__":
    main()

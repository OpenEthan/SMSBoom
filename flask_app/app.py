# encoding=utf8
import json
import time
from flask import Flask, make_response, request, jsonify, render_template
from flask_cors import CORS
from urllib3 import disable_warnings

from utils import *

disable_warnings()

app = Flask(__name__)
CORS(app, supports_credentials=True, resources="/*")  # 跨域

# 解决与 vue 冲突
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'

def request_parse(req_data: request) -> dict:
    '''解析请求数据并以字典的形式返回'''
    if req_data.method == 'POST':
        data = req_data.form

    elif req_data.method == 'GET':
        data = req_data.args

    return dict(data)


class BaseResponse(BaseModel):
    """返回的响应"""
    status: int = 0  # 状态码 0-->成功 1-->失败
    msg: str = "前端显示的简短信息"
    data: Optional[str]

    @property
    def resp(self):
        '''BaseModel类型返回json'''
        response = make_response(
            json.dumps(
                self.dict(),
                ensure_ascii=False,
                sort_keys=False
            ),
        )
        response.mimetype = 'application/json'
        # 跨域设置
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,GET,POST'
        response.headers['Access-Control-Allow-Headers'] = 'x-requested-with'
        return response


@app.route("/", methods=['GET'])
def index():
    return render_template('admin.html')

@app.route("/testapi/", methods=['POST'])
def testapi():
    brs = BaseResponse()
    # 需要传入 json 数据
    try:
        jsonData = request.get_json()
        api = API(**jsonData)
        phone = jsonData.get('phone')
        if not phone:
            raise ValueError("参数 phone 没有！")
        try:
            resp = test_resq(api, phone)
            brs.status = 0
            brs.msg = f"请求成功！{resp}"
            brs.data = resp.text
        except Exception as why:
            brs.status = 1
            brs.msg = f"请求失败：{why}"
    except Exception as why:
        brs.status = 1
        brs.msg = f"参数有误：{why}"
    return brs.resp


@app.route("/submitapi/", methods=['POST'])
def submitapi():
    """提交API到json文件"""
    # 需要传入 json 数据
    jsonData = request.get_json()
    api = API(**jsonData).handle_API()
    data = json.loads(json_path.read_text(encoding='utf8'))
    with open(json_path, mode="w", encoding="utf8") as j:
        try:
            data.append(api.dict())
            json.dump(data, j, ensure_ascii=False, sort_keys=False)
            return BaseResponse(status=0, msg="写入成功!").resp
        except Exception as why:
            return BaseResponse(status=1, msg=f"写入失败!{why}").resp


@app.route("/backapi/", methods=['GET', 'POST'])
def backjson():
    """备份json文件"""
    try:
        timeStruct = time.localtime(int(time.time()))
        strTime = time.strftime("%Y_%m_%d_%H_%M_%S", timeStruct)
        Path(json_path.parent, 'apiback').mkdir(exist_ok=True)
        json_back_path = Path(json_path.parent, 'apiback',
                              f"api_back_{strTime}.json")
        with open(json_back_path, mode="w") as j:
            j_data = json.loads(json_path.read_text(encoding='utf8'))
            json.dump(j_data, j, ensure_ascii=False, sort_keys=False)
        return BaseResponse(status=0, msg="备份成功!").resp
    except Exception as why:
        return BaseResponse(status=1, msg=f"备份失败{why}").resp


@app.route("/downloadapi/", methods=['GET'])
def downloadapi():
    """下载接口文件"""
    return json_path.read_text(encoding='utf8')


app.run(host="0.0.0.0", port=10981, debug=True)

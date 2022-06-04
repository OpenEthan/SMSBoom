# encoding=utf8
# flask app views
from . import main
import json
from ..model import Apis, API
from ..utils import test_resq
from .. import logger
import httpx
from flask_app import db
from flask import request, jsonify


@main.route("/", methods=['GET', 'POST'])
def index():
    return "index"


@main.route("/testapi/", methods=['GET', 'POST'])
def testapi():
    try:
        req = request.json
        api = API(**req)
        resp = test_resq(api, phone=req.get('phone'))
        print(resp.text)
        return jsonify({"status": 0, "resp": f"{resp.text}"})
    except httpx.HTTPError as why:
        return jsonify({"status": 1, "resp": f"HTTP请求错误:{why}"})
    except Exception as why:
        logger.exception(why)
        return jsonify({"status": 1, "resp": f"其他错误:{why}"})

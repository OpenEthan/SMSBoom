# encoding=utf8
# app 工厂函数
from flask import Flask,current_app
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_babelex import Babel
import sys
import os
from loguru import logger


# 判断系统
WIN = sys.platform.startswith('win')
if WIN:  # 如果是 Windows 系统，使用三个斜线
    prefix = 'sqlite:///'
else:  # 否则使用四个斜线
    prefix = 'sqlite:////'

# 日志处理
logger.remove()
logger.add(
    sink=sys.stdout,
    format="<green>{time:YYYY-MM-DD at HH:mm:ss}</green> - <level>{level}</level> - <level>{message}</level>",
    colorize=True,
    backtrace=True
)

app = Flask(__name__)


# app config
class AppConfig:
    SQLALCHEMY_DATABASE_URI = prefix + \
        os.path.join(app.root_path, 'data.db')  # 数据库路径
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 关闭对模型修改的监控
    FLASK_ADMIN_SWATCH = "cerulean"  # admin 主题

    # 密钥
    SESSION_TYPE = 'filesystem'
    SECRET_KEY = os.urandom(24)

    BABEL_DEFAULT_LOCALE = 'zh_CN'  # 汉化

    TEST_PHONE = "19820294268"  # 测试手机号


app.config.from_object(AppConfig)
# 设置模板全局变量
# print(app.config.get("TEST_PHONE"))
app.add_template_global(current_app,"current_app")

# 扩展
db = SQLAlchemy(app)
babel = Babel(app)

admin = Admin(app, name="短信接口调试", template_mode='bootstrap3')
from .model import ApisModelVies, Apis
admin.add_view(ApisModelVies(Apis, db.session))

# buleprint
from .views import main as main_blueprint
app.register_blueprint(main_blueprint)

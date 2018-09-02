from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    # 设置配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    # 使用蓝图注册视图函数
    register_blueprint(app)

    db.init_app(app)
    db.create_all(app=app)
    return app


# 注册视图函数
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)

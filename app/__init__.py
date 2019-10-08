from flask import Flask
from app.models.book import db

def create_app():
    # 下面这个app叫做核心对象，可以注册各种插件，比如蓝图
    app = Flask(__name__)
    # 导入配置文件模块的路径
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    # 将蓝图和核心对象关联起来
    register_blueprint(app)

    # 把数据库和核心对象关联起来
    db.init_app(app)
    db.create_all(app=app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)

from flask import Flask


def create_app():
    # 下面这个app叫做核心对象，可以注册各种插件，比如蓝图
    app = Flask(__name__)
    # 导入配置文件模块的路径
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app

def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)

from flask import Flask, current_app

app = Flask(__name__)
# flask中有两种上下文：
# 应用上下文，是一个对象
# 请求上下文，是一个对象
# 在离线应用，单元测试中需要用到

# 对于实现了上下文协议的对象，都可以使用with
with app.app_context():
    a = current_app
    b = current_app.config['DEBUG']

from app import create_app

app = create_app()

if __name__ == '__main__':
    # 在生产环境中，使用nginx（用来接收浏览器发来的请求，并转发给uwsgi）+uwsgi
    # 启用flask的调试模式，更改代码以后，服务器就会重启
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'], threaded=True)


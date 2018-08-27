from flask import Flask

app = Flask(__name__)
# 设置配置文件
app.config.from_object('config')

# app.add_url_rule('/hello', view_func=hello)
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)

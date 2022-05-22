from flask import Flask, request
from flasgger import Swagger, swag_from

app = Flask(__name__)
swagger = Swagger(app)
'''
利用flasagger开源脚手架，将自己写的一个api同步生成一个swagger上，实现api开发文档先行，同时生成，同时成立
'''

# 云你好服务 API 接口
@app.get("/api/v1/hello")
@swag_from('hello.yml')
def hello():
    try:

        # 看用户是否传递了参数，参数为打招呼的目标
        name = request.args.get("name", "")

        # 如果传了参数就向目标对象打招呼，输出 Hello XXX，否则输出 Hello World
        return f"Hello {name}" if name else "Hello World", 200

    except Exception:
        # 假设在使用云你好服务的过程中出现了异常
        return "sorry～服务器开小差了", 500


if __name__ == '__main__':
    app.run()
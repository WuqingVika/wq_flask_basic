# -*- coding:utf-8 -*-
__author__ = 'qwu'
__date__ = '2020/3/31 14:43'

# -*- coding: utf-8 -*-
from flask import Flask, Blueprint
from UserController import userService
app = Flask(__name__)


app.register_blueprint(userService, url_prefix="/user")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

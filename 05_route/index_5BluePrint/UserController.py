# -*- coding:utf-8 -*-
__author__ = 'qwu'
__date__ = '2020/3/31 14:43'

# -*- coding: utf-8 -*-
from flask import Flask,Blueprint
app = Flask( __name__ )

userService = Blueprint( "user",__name__ )
@userService.route( "/list" )
def userList():
    return r'返回用户信息列表'


@userService.route( "/one" )
def user():
    return r'访问"http://127.0.0.1:5000/user/one"返回小吴'



# coding: utf-8
from sqlalchemy import Column, Integer, String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class SysUserInfo(db.Model):
    __tablename__ = 'sys_user_info'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

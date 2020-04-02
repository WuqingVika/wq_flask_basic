# -*- coding: utf-8 -*-
from application import db


class sys_user_info(db.Model):
    id = db.Column(db.INTEGER(), primary_key=True)
    name = db.Column(db.String(120))

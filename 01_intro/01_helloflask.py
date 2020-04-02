# -*- coding:utf-8 -*-
__author__ = 'qwu'
__date__ = '2020/3/30 10:49'

from flask import Flask

app = Flask(__name__)
app.config.from_envvar("ops_config")
@app.route("/")
def hello():
    return "hello flask,hello wuqingvika~"


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port=6543)
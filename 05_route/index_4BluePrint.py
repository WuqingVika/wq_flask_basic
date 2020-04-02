# -*- coding: utf-8 -*-
from flask import Flask,Blueprint
app = Flask( __name__ )

index_page = Blueprint( "index_page",__name__ )
@index_page.route( "/" )
def index_page_index():
    return r'访问"http://127.0.0.1:5000/bluePrint/"，就能看到我index page'

app.register_blueprint( index_page,url_prefix = "/bluePrint" )

@app.route( "/" )
def hello():
    return "Hello ,I Love wuqingvika"


if __name__ == "__main__":
    app.run( host = "0.0.0.0",debug=True )
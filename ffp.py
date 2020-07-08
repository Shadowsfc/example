# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:52:37 2020

@author: a783270
"""

from flask import json
from flask import request
from flask import Flask

app = Flask(__name__)

@app.route('/')
def api_root():
   
    return "welcome"
@app.route('/github', method=['POST'])
def api_gh_message():
    if request.headers['Content-type'] == 'application/json':
        my_info = json.dumps(request.json)
        print(my_info)
        return my_info
if __name__ == '__main__':
    app.run('localhost',5000)
    
 
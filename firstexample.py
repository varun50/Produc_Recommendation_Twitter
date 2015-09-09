# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 12:29:48 2014

@author: Owner
"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
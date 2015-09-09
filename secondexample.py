# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 12:33:16 2014

@author: Owner
"""

from flask import Flask, render_template, request, redirect, url_for, abort, session, make_response
from query import run_query
from werkzeug.wrappers import Request, Response

app = Flask(__name__)
app.config['SECRET_KEY'] = 'F34TF$($e34D';

@app.route('/data', methods=['GET'])
def data():
    Product_Type = request.args.get('Product_type')
    Product_Name = request.args.get('Product_Name')

@app.route('/')    
def home():
    print 'Here i am this is me'
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST' ])
def search():
   if request.method == 'POST':
    Product_Name = request.form['Product_Name']
    print 'productname', Product_Name
    result = run_query(Product_Name)
    print result
    #return render_template('message.html')
    #return render_template('index.html')
    return Response(result)
    #return render_template('message.html')#, result=result)

@app.route('/message')
def message():
    if not 'Product_Type' in session:
        return abort(403)
    return render_template('message.html', username=session['Product_Type'], 
                                           message=session['Product_Name'])


if __name__ == '__main__':
   app.run(debug=True, port=8080)
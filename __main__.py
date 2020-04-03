#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:13:55 2020

@author: brian
"""


from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
#!flask/bin/python2.7

"""
.. :module: run.py
   :platform: Linux
   :synopsis: sample web app
.. moduleauthor: Rob Katcher <rob.katcher@gmail.com> (Jan 15, 2017)
"""

import os
from flask import Flask
from flask import request
from flask import send_from_directory
import requests
import pusher
import json


app = Flask(__name__)

# sample GET returns text
@app.route("/")
def welcome():
    return "Welcome to your sample app!"

# sample GET returns web page
@app.route('/')
def home():
    return send_from_directory('docs', 'home.htm')

# sample POST returns name field
@app.route("/dataReceive", methods = ['POST'])
def dataReceive():
    # placeholder for receiving data
    name=request.form.get('name', 'no name provided!')
    return name

    # payload = request.data
    # payload = json.loads(payload)
    # data = payload['data']
    # return data['name']


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


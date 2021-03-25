#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask
import requests
import json
from app.utils.read_file import encode_base64, decode_base64, read_img, printosinfo
import os
import sys

app = Flask(__name__)


@app.route('/')
def home_page():
    return 'Hi Python'


@app.route('/layui')
def layui_api():
    url = 'https://www.layui.com/demo/table/user/?page=1&limit=30'
    r = requests.get(url)
    print(type(r.json()))
    return r.json()


if __name__ == '__main__':
    # en_img = encode_base64('./images/icic.png')
    # decode_base64(en_img)
    # txt_data = read_img('./static/t.txt')
    # decode_base64(txt_data)
    # print(txt_data)
    # printosinfo()
    app.run(debug=True)

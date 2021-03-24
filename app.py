#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from flask import Flask
import requests,json
import base64
import time

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

def encode_base64(file):
    with open(file,'rb') as f:
        img_data = f.read()
        base64_data = base64.b64encode(img_data)
        print(type(base64_data))
        #print(base64_data)
        # 如果想要在浏览器上访问base64格式图片，需要在前面加上：data:image/jpeg;base64,
        base64_str = str(base64_data, 'utf-8')  
        print(base64_str)
        return base64_data

def decode_base64(base64_data):
    ticks = time.time()
    with open('./images/'+ str(ticks) +'.jpg','wb') as file:
        img = base64.b64decode(base64_data)
        file.write(img)

def read_img(file_url):
    with open(file_url,'r') as file:
        file_data = file.read()
        return file_data.replace('data:image/png;base64,','')

if __name__ == '__main__':
    # en_img = encode_base64('./icic.png')
    # decode_base64(en_img)
    txt_data = read_img('./static/t.txt')
    decode_base64(txt_data)
    print(txt_data)
    app.run(debug=True)
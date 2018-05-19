# -*- coding: utf-8 -*-
import sys
import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from flask import Flask, request, jsonify
import urllib.request
import text_recog 
import json
import caipin

app = Flask(__name__)

@app.route('/image', methods=['POST'])
def iamge_query():
    # print(request.json) # some kinds of query
    fod_name = recog_image(image)
    # req = request.json
    res = {}
    res['result'] = {}
    try:
        query_name = fod_name
        query_result_ = text_recog.query_search(query_name)
        query_result = query_result_.strip().split('\t')
        if len(query_result) < 3:
            return query_result_
        res['result']['name']= query_result[0]
        res['result']['description']= query_result[1]
        res['result']['material-1']= query_result[2]
        res['result']['material-2']= query_result[3]
        res['result']['link']= query_result[4]
        res['status'] = 0
        res['message'] = '成功'
        print(res)
        return json.dumps(res)
    except Exception as e:
        print(e)
        res['status'] = 1
        res['message'] = '计算失败'
        print(res)
        return json.dumps(res)


@app.route('/text', methods=['POST'])
def text_query():
    print(request.json)
    req = request.json
    res = {}
    res['result'] = {}
    try:
        query_name = req['food_name']
        query_result_ = text_recog.query_search(query_name)
        query_result = query_result_.strip().split('\t')
        if len(query_result) < 3:
            res['result']['name']= 'not exit'
            res['result']['description']= query_result_
            res['result']['material-1']= 'not exit'
            res['result']['material-2']= 'not exit'
            res['result']['link']= 'not exit'
            res['status'] = 0
            res['message'] = '成功'
            print(res)
            return json.dumps(res)
        res['result']['name']= query_result[0]
        res['result']['description']= query_result[1]
        res['result']['material-1']= query_result[2]
        res['result']['material-2']= query_result[3]
        res['result']['link']= query_result[4]
        res['status'] = 0
        res['message'] = '成功'
        print(res)
        return json.dumps(res)
    except Exception as e:
        print(e)
        res['status'] = 1
        res['message'] = '计算失败'
        print(res)
        return json.dumps(res)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 8021)
        

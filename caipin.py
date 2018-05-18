# -*- coding: utf-8 -*-
import sys
import io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import requests
import json
import base64
import urllib
from aip import AipImageClassify


def get_access_token():
     #这里添上自己的app数据就ok
     APP_ID = '11257841'
     API_KEY = '4afbHaeDovOXIquc9k0vpxNc'
     SECRET_KEY = 'd7WePS3GScf6lxOe2M6aC1Lp3VdDv2rw'

     url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s' % (API_KEY, SECRET_KEY)
     response = requests.post(url)

     access_token = response.content.decode('utf-8')
     access_token = json.loads(access_token)

     access_token = str(access_token['access_token'])

     return access_token

def get_file_content(filePath):
     with open(filePath,'rb') as fp:
          return fp.read()

def get_recognization(access_token):
     host = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish?access_token=' + access_token
     header = {'Content-Type' : 'appliapplication/x-www-form-urlencodedcation/x'}

     #这里改成自己的文件路径
     # image = get_file_content('/home/pi/pythoncode/download.jpg')
     image = get_file_content('test.jpg') # how to get a picture
     image = base64.b64encode(image)
     body = {'image' : image, 'top_num' : 1}
     body = urllib.parse.urlencode(body)

     response = requests.post(host,data=body,headers=header)
     response = json.loads(response.text)
     name = response['result'][0]['name']

     return name

def get_recognization_server(access_token, iamge):
     host = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish?access_token=' + access_token
     header = {'Content-Type' : 'appliapplication/x-www-form-urlencodedcation/x'}

     #这里改成自己的文件路径
     # image = get_file_content('/home/pi/pythoncode/download.jpg')
     image = get_file_content('test.jpg') # how to get a picture
     image = base64.b64encode(image)
     body = {'image' : image, 'top_num' : 1}
     body = urllib.parse.urlencode(body)

     response = requests.post(host,data=body,headers=header)
     response = json.loads(response.text)
     name = response['result'][0]['name']

     return name
     


def main():
     at = get_access_token()
     recognization = get_recognization(at)
     print(recognization)

def recog_image(image):
     at = get_access_token()
     result = get_recognization_server(at, iamge)
     print(result)
     return result
     

#if __name__ == '__main__':
#      main()
                 

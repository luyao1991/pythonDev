# coding:utf-8
import requests

data = {
    '3': '4',
    'c': 'd',
}
url = 'http://127.0.0.1:8888/request'
response = requests.post(url, data)
print(response.text)

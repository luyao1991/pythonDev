# coding:utf-8
# @File:  news.py
# @Author:  guozhiwen
# @Date:  2019/1/13
# @Time:  1:39 PM
# @Version:  v3.6.4

from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from get_data import GetData
import json

app = Flask(__name__)


@app.route('/news')
def show():
    return render_template('news.html')


@app.route('/api/v1/get_news')
def get_news():
    data = request.values.to_dict()
    page = int(data.get('page', 0))
    # with open('/Users/shogakusha/Workspaces/github/pythonDev/python/day10/static/data.json') as f:
    #     lines = f.readlines()
    #     print(len(lines))
    #     data = list(map(json.loads, lines))
    try:
        news = GetData()
        results = news.get(page)
        return jsonify({
            'status': 0,
            'message': 'success',
            'data': results
        })
    except Exception as error:
        return jsonify({
            'status': 500,
            'message': str(error),
            'data': results
        })


@app.route('/api/v1/search_news')
def search_news():
    pass


if __name__ == '__main__':
    app.run(
        debug=True,
        port=8889
    )

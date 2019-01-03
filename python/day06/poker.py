# coding:utf-8
import sys, os
import flask
import random
from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template

from rule import Rule

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = {
        'index': random.randint(100000, 1000000),
        'name': 'Jason',
        'first': False,
        'visit': [
            {'url': '/index', 'title': "首页"},
            {'url': '/poker', 'title': "扑克"},
            {'url': '/info', 'title': "信息"}
        ]
    }
    return render_template("index.html", user=user)


@app.route('/count/<user>')
def user_count(user):
    index = random.randint(1, 10000)
    return '恭喜{0}是访问的第{1}个用户'.format(user, index)


@app.route('/poker')
def poker():
    directory = os.listdir('./static/poker/')
    return "<img src='/static/poker/{0}'/> ".format(random.choice(directory))


@app.route('/info')
def info():
    return jsonify({
        'status': 0,
        'message': 'Success',
        'data': {
            'python': '.'.join(map(str, sys.version_info[0:3])),
            'flask': flask.__version__
        }
    })


@app.route('/request', methods=['GET', 'POST'])
def request_test():
    data = {
        'path': request.path,
        'method': request.method,
        'params': request.values
    }
    return jsonify({
        'status': 0,
        'message': 'Success',
        'data': data
    })


@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), error.code


@app.route('/game')
def game():
    rule = Rule()
    player1 = rule.deal()[0]
    player2 = rule.deal()[1]
    status = 1
    return render_template('game.html', player1=player1, player2=player2, status=status)


if __name__ == '__main__':
    app.run()

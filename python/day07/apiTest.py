# coding:utf-8
from flask import render_template
from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)


@app.route('/')
def api_test():
    return render_template("apiTest.html")


@app.route('/accept', methods=["POST"])
def accept():
    # data = request.values.to_dict()
    data = request.get_json()
    print(data)
    if data == {}:
        return jsonify({
            'status': 400,
            'message': 'miss param',
            'data': 0
        })
    else:
        return jsonify({
            'status': 200,
            'message': 'success',
            'data': data
        })


if __name__ == '__main__':
    app.run(
        port=8888,
        debug=True,
    )

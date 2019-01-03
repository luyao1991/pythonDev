# coding:utf-8
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/')
@app.route('/calculator')
def calculator():
    return render_template('calculator.html')


@app.route('/evaluation')
def evaluation():
    data = request.values.to_dict()
    print(data)
    if 'expression' not in data:
        return jsonify({
            'status': 400,
            'message': 'miss param',
            'data': 0
        })
    else:
        try:
            result = eval(data['expression'])
            return jsonify({
                'status': 200,
                'message': 'Success',
                'data': result
            })
        except SyntaxError:
            return jsonify({
                'status': 500,
                'message': 'Success',
                'data': data['expression']
            })


if __name__ == '__main__':
    app.run(
        port=8889,
        debug=True,
        threaded=2
    )

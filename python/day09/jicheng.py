# coding:utf-8
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def jicheng():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(
        port=8889,
        debug=True
    )

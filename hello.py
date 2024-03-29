"""
패스트캠퍼스 API
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """
    hello world api
    """
    return "<p>Hello, World!</p>"
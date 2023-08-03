from flask import Flask, jsonify
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)


@app.route('/home/', methods=['POST'])
def home():
    response = jsonify({"message": "You are in Home Page"})
    response.headers['x-frame-options'] = "X"
    response.headers['x-content-type-options'] = "X"
    response.headers['referrer-policy'] = "X"
    response.headers['cross-origin-opener-policy'] = "X"
    return response


asgi_app = WsgiToAsgi(app)


async def app(scope, receive, send):
    await asgi_app(scope, receive, send)

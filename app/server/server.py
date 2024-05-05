import json
from flask import Flask, Response

class Server:

    def __init__(self):
        self.app = Flask(__name__)

        self.register_endpoints()

    def register_endpoints(self):
        self.app.add_url_rule(
            rule="/",
            endpoint="test",
            view_func=self.test,
            methods=["GET"]
        )

    def test(self):
        body = {
            "test": "hello"
        }
        resp = Response(
            response=json.dumps(body), status=200, mimetype="application/json")
        return resp

    def run(self):
        self.app.run(debug=False, port=8080)

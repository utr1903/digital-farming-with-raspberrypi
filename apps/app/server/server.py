import json

from waitress import serve
from flask import Flask, Response

class Server:

    def __init__(self):
        self.app = Flask(__name__)
        self.app.debug = False
        self.app.use_reloader = False
        self.register_endpoints()

    def register_endpoints(self):
        self.app.add_url_rule(
            rule="/",
            endpoint="ping",
            view_func=self.ping,
            methods=["GET"]
        )

    def ping(self):
        body = {"ping": "pong"}
        resp = Response(
            response=json.dumps(body),
            status=200,
            mimetype="application/json",
        )
        return resp

    def run(self):
        serve(self.app, host="127.0.0.1", port=8080)

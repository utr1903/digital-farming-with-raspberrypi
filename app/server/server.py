import json
from flask import Flask, Response

class Server:

    def __init__(self):
        self.app = Flask(__name__)
        self.register_endpoints()
    
    def __init__(self, db_prometheus):
        self.app = Flask(__name__)
        self.register_endpoints()
        self.db_prometheus = db_prometheus

    def register_endpoints(self):
        self.app.add_url_rule(
            rule="/",
            endpoint="ping",
            view_func=self.ping,
            methods=["GET"]
        )
        self.app.add_url_rule(
            rule="/metrics",
            endpoint="metrics",
            view_func=self.metrics,
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

    def metrics(self):
        body = self.db_prometheus.generate_latest()
        resp = Response(
            response=body,
            status=200,
            mimetype="text/plain",
        )
        return resp

    def run(self):
        self.app.run(debug=False, port=8080)

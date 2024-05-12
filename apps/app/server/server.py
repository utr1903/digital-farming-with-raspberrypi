import logging
import json

from waitress import serve
from flask import Flask, request, Response

logger = logging.getLogger(__name__)

class Server:

    def __init__(self, actor_svc):
        self.app = Flask(__name__)
        self.app.debug = False
        self.app.use_reloader = False
        self.register_endpoints()

        self.actor_service = actor_svc

    def register_endpoints(self):
        self.app.add_url_rule(
            rule="/",
            endpoint="ping",
            view_func=self.ping,
            methods=["GET"]
        )
        self.app.add_url_rule(
            rule="/actor",
            endpoint="actor",
            view_func=self.actor,
            methods=["POST"]
        )

    def ping(self):
        body = {"ping": "pong"}
        resp = Response(
            response=json.dumps(body),
            status=200,
            mimetype="application/json",
        )
        return resp
    
    def actor(self):
        body = request.json
        logger.debug(body)

        if body["state"] == "alerting":
            if body["receiver"] == "Humidity too low":
                running_actor_succeeded = self.actor_service.run_actor("actor1")
                if running_actor_succeeded == False:
                    return Response(
                        response=json.dumps({
                            "result": "Failed."
                        }),
                        status=500,
                        mimetype="application/json",
                    )

        return Response(
            response=json.dumps({
                "result": "Suceeded."
            }),
            status=202,
            mimetype="application/json",
        )

    def run(self):
        serve(self.app, host="127.0.0.1", port=8080)

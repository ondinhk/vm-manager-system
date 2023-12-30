import json
import time

import zmq
from app.log import logger


class ZeroMQ:
    def __init__(self):
        self.context = zmq.Context()
        self.publisher = self.context.socket(zmq.PUB)
        self.publisher.bind("tcp://0.0.0.0:6000")
        logger.info("Init master queue success")

    def publish_message(self, data: dict):
        message = json.dumps(data)
        self.publisher.send_string(message)
        logger.info(f"Publishing: {message}")

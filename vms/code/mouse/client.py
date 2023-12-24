import json
import os

import zmq
from pynput.mouse import Controller, Button

from log import logger

mouse_queue = os.getenv("MOUSE_QUEUE")

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect(f"tcp://{mouse_queue}")
subscriber.setsockopt_string(zmq.SUBSCRIBE, '')

# Create a mouse controller
mouse = Controller()
keyboard = Controller()


def match_action(action):
    logger.info(action)


logger.info('Client run sync mouse success')

while True:
    message = subscriber.recv_string()
    data = json.loads(message)
    x, y, dx, dy = data['data'].split(',')
    # Right
    if data.get('actions', None) == 'right' and data.get('pressed', None):
        mouse.position = (int(x), int(y))
        mouse.press(Button.right)
    if data.get('actions', None) == 'right' and not data.get('pressed', None):
        mouse.position = (int(x), int(y))
        mouse.release(Button.right)
    # Left
    if data.get('actions', None) == 'left' and data.get('pressed', None):
        mouse.position = (int(x), int(y))
        mouse.press(Button.left)
    if data.get('actions', None) == 'left' and not data.get('pressed', None):
        mouse.position = (int(x), int(y))
        mouse.release(Button.left)
    # Left
    if data.get('actions', None) == 'middle' and data.get('pressed', None):
        mouse.position = (int(x), int(y))
        mouse.press(Button.middle)
    if data.get('actions', None) == 'middle' and not data.get('pressed', None):
        mouse.position = (int(x), int(y))
        mouse.release(Button.middle)
    # Scroll
    if data.get('actions', None) == 'scroll':
        mouse.position = (int(x), int(y))
        mouse.scroll(int(dx), int(dy))
    logger.info(data)

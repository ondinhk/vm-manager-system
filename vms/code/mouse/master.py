import json
import threading
import time

import zmq
from pynput import mouse, keyboard
from pynput.mouse import Button

from log import logger


class ZeroMQ:
    def __init__(self):
        self.context = zmq.Context()
        self.publisher = self.context.socket(zmq.PUB)
        self.publisher.bind("tcp://0.0.0.0:5000")
        logger.info("Master VM, Init master queue success")

    def publish_message(self, data: dict):
        try:
            message = json.dumps(data)
            self.publisher.send_string(message)
            logger.info(f"Publishing: {message}")
        except Exception as e:
            logger.error(e)
            pass


master = ZeroMQ()

is_send = False


def on_click(x, y, button, pressed):
    # Right
    if button == Button.right and is_send:
        if pressed:
            data = {'actions': 'right', 'data': f'{x},{y},_,_', 'pressed': True}
            master.publish_message(data)
        else:
            data = {'actions': 'right', 'data': f'{x},{y},_,_', 'pressed': False}
            master.publish_message(data)
    # Left
    if button == Button.left and is_send:
        if pressed:
            data = {'actions': 'left', 'data': f'{x},{y},_,_', 'pressed': True}
            master.publish_message(data)
        else:
            data = {'actions': 'left', 'data': f'{x},{y},_,_', 'pressed': False}
            master.publish_message(data)
    # Middle
    if button == Button.middle and is_send:
        if pressed:
            data = {'actions': 'middle', 'data': f'{x},{y},_,_', 'pressed': True}
            master.publish_message(data)
        else:
            data = {'actions': 'middle', 'data': f'{x},{y},_,_', 'pressed': False}
            master.publish_message(data)


def on_scroll(x, y, dx, dy):
    data = {'actions': 'scroll', 'data': f'{x},{y},{dx},{dy}', 'pressed': False}
    if is_send:
        master.publish_message(data)

def on_press(key):
    global is_send
    try:
        if key.char == '/':
            is_send = not is_send
    except AttributeError:
        pass


mouse_listener = mouse.Listener(on_click=on_click, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_press) 

# Start both listeners in separate threads
mouse_thread = threading.Thread(target=mouse_listener.run)
keyboard_thread = threading.Thread(target=keyboard_listener.run)

# Start
mouse_thread.start()
keyboard_thread.start()

# Wait for both threads to finish
mouse_thread.join()
keyboard_thread.join()

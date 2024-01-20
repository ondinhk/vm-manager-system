import asyncio
import json
import os

import zmq

from app.logger import logger
from app.services.chrome.chrome_service import ChromeService
from app.services.keyboard_service import KeyboardService
from app.services.screen.screen_service import ScreenService

master_queue = os.getenv("MASTER_QUEUE")
context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect(f"tcp://{master_queue}")
subscriber.setsockopt_string(zmq.SUBSCRIBE, '')


def default_action():
    logger.info("Invalid actions")


def match_action(action: str, _data: dict):
    action_dict = {
        'chrome-open': ChromeService.open_chrome,
        'chrome-actions': ChromeService.actions_chrome,
        'chrome-close': ChromeService.close_chrome,
        'chrome-youtube': ChromeService.open_youtube,
        'chrome-proxy': ChromeService.open_proxy,
        'chrome-proxy-refresh': ChromeService.refresh_proxy,
        'take-screen': ScreenService.take_screen
    }
    return asyncio.run(action_dict.get(action, default_action)())


logger.info('Worker connect backend for sync action success')
while True:
    try:
        message = subscriber.recv_string()
        data = json.loads(message)
        logger.info(data)
        if data.get('action', None) == 'input-value':
            KeyboardService().input_text(data.get('data', None)),
        else:
            match_action(action=data.get('action'), _data=data)
    except Exception as e:
        logger.error(e)
        continue

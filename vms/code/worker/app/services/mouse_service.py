import asyncio
import time

import cv2
import numpy as np
import pyautogui
from app.logger import logger
from app.ultis.constants import CONFIDENCE_THRESHOLD

pyautogui.FAILSAFE = False


class MouseService:
    @classmethod
    async def click_image(cls, image_path, index=0):
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save("/home/ubuntu/code/worker/app/services/chrome/images/test.PNG")
            screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
            template = cv2.imread(image_path)
            result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            if max_val >= CONFIDENCE_THRESHOLD:
                logger.info(f'Found image CONFIDENCE_THRESHOLD is {max_val}')
                template_center_x = max_loc[0] + template.shape[1] // 2
                template_center_y = max_loc[1] + template.shape[0] // 2
                logger.info(f"x {template_center_x} - y {template_center_y} type {type(template_center_y)}")
                await cls.click_and_move_position(template_center_x, template_center_y)
                return True
            raise Exception(f"Not found image CONFIDENCE_THRESHOLD is {max_val}")
        except Exception as e:
            if index == 3:
                return False
            logger.error(e)
            logger.info(f"Try to find frame: {image_path} - {index} times")
            index += 1
            time.sleep(1)
            await cls.click_image(image_path, index)

    @classmethod
    async def click_position(cls, x: int, y: int, middle=False):
        if middle:
            pyautogui.click(x, y, button='middle')
        else:
            pyautogui.click(x, y)
        await asyncio.sleep(1)

    @classmethod
    async def click_and_move_position(cls, x: int, y: int, middle=False):
        await cls.move_diagonal_to_end(x, y)
        if middle:
            pyautogui.click(x, y, button='middle')
        else:
            pyautogui.click(x, y)
        await asyncio.sleep(1)

    @classmethod
    async def move_diagonal_to_end(cls, end_x, end_y, steps=100):
        start_x, start_y = pyautogui.position()
        for i in range(steps + 1):
            x = int(start_x + (end_x - start_x) * (i / steps))
            y = int(start_y + (end_y - start_y) * (i / steps))
            pyautogui.moveTo(x, y)
            await asyncio.sleep(0.02)

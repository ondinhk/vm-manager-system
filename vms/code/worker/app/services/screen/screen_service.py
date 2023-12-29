import os

import pyautogui


class ScreenService:

    @classmethod
    async def take_screen(cls):
        screenshot = pyautogui.screenshot()
        name = os.getenv('VM_NAME')
        screenshot.save(f"/home/ubuntu/code/images/{name}.PNG")

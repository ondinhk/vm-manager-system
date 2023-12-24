import asyncio
import os
import subprocess

from app.services.keyboard_service import KeyboardService
from pynput.keyboard import Key

from app.services.mouse_service import click_position


class ChromeService:

    @classmethod
    async def open_chrome(cls):
        url = 'https://google.com/'
        chrome_path = '/usr/bin/google-chrome-stable'
        proxy = os.getenv('HTTP_PROXY')
        command = [chrome_path, '--no-sandbox', url] if url else [chrome_path]
        if proxy:
            command = [chrome_path, '--no-sandbox', url, f'--proxy-server={proxy}'] if url else [chrome_path]
        subprocess.Popen(command, close_fds=True, start_new_session=True)

    @classmethod
    async def login_chrome(cls):
        await asyncio.sleep(2)
        is_clicked = click_position(x=749, y=142)
        email = os.getenv('EMAIL')
        password = os.getenv('PASSWORD')
        if is_clicked and email and password:
            await asyncio.sleep(5)
            KeyboardService().input_text(email)
            await asyncio.sleep(5)
            KeyboardService().enter_press()
            await asyncio.sleep(15)
            KeyboardService().input_text(password)
            await asyncio.sleep(3)
            KeyboardService().enter_press()
            return True
        return False

    @classmethod
    async def open_youtube(cls):
        await asyncio.sleep(2)
        KeyboardService().auto_press_key(Key.f6)
        await asyncio.sleep(2)
        KeyboardService().input_text('https://youtube.com')
        await asyncio.sleep(2)
        KeyboardService().enter_press()
        return True

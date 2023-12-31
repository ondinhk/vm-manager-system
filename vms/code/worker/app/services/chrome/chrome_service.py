import asyncio
import os
import subprocess

from app.logger import logger
from app.services.keyboard_service import KeyboardService
from pynput.keyboard import Key

from app.services.mouse_service import MouseService
from app.ultis.helper import sleep_random


class ChromeService:

    @classmethod
    async def open_chrome(cls):
        await sleep_random(min_wait=5, max_wait=60)
        chrome_path = '/usr/bin/google-chrome'
        command = [chrome_path, '--no-sandbox']
        # Todo if we have a proxies :((
        # proxy = 'http://104.19.112.172:80'
        # if proxy:
        #     command = [chrome_path, '%U', '--no-sandbox', f'--proxy-server={proxy}']
        subprocess.Popen(command, close_fds=True, start_new_session=True)
        # Close warning no-sandbox
        await asyncio.sleep(5)
        await MouseService.click_position(x=775, y=148)
        await cls.click_blank_page()

    @classmethod
    async def login_chrome(cls):
        await sleep_random(min_wait=5, max_wait=60)
        KeyboardService().auto_press_key(Key.f6)
        KeyboardService().input_text('https://google.com')
        KeyboardService().enter_press()
        is_clicked = await MouseService.click_position(x=749, y=142)
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
        await sleep_random(min_wait=5, max_wait=60)
        KeyboardService().auto_press_key(Key.f6)
        await asyncio.sleep(2)
        KeyboardService().input_text('https://youtube.com')
        await asyncio.sleep(2)
        KeyboardService().enter_press()
        return True

    @classmethod
    async def open_proxy(cls):
        # Click popup vpn
        await MouseService.click_position(x=616, y=64)
        # Check group
        await cls.select_proxy()
        # Click start
        await sleep_random(min_wait=10, max_wait=25)
        await MouseService.click_position(x=490, y=230)
        await sleep_random(min_wait=10, max_wait=25)
        # Close app
        await cls.click_blank_page()

    @classmethod
    async def select_proxy(cls):
        current_group = os.getenv('GROUP')
        # Click open select
        await MouseService.click_position(x=480, y=385)
        await asyncio.sleep(4)
        if current_group == 'group_fr':
            await MouseService.click_position(x=500, y=220)
        elif current_group == 'group_nether':
            await MouseService.click_position(x=500, y=250)
        elif current_group == 'group_rus':
            await MouseService.click_position(x=500, y=290)
        elif current_group == 'group_sing':
            await MouseService.click_position(x=500, y=320)
        elif current_group == 'group_uk':
            await MouseService.click_position(x=500, y=360)
        elif current_group == 'group_us_vir':
            await MouseService.click_position(x=500, y=390)
            await MouseService.click_position(x=500, y=430)
        elif current_group == 'group_us_ore':
            await MouseService.click_position(x=500, y=390)
            await MouseService.click_position(x=500, y=460)
        else:
            return

    @classmethod
    async def click_blank_page(cls):
        await MouseService.click_position(x=40, y=135)

    @classmethod
    async def refresh_proxy(cls):
        # Click popup vpn
        await MouseService.click_position(x=616, y=64)
        # Click stop
        await sleep_random(min_wait=10, max_wait=25)
        await MouseService.click_position(x=490, y=230)
        await sleep_random(min_wait=10, max_wait=25)
        # Click Start
        await MouseService.click_position(x=490, y=230)
        await sleep_random(min_wait=10, max_wait=25)
        # Close app
        await cls.click_blank_page()
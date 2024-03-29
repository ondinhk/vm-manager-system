import asyncio
import os
import random
import subprocess
import time

from pynput.keyboard import Key
from pynput.mouse import Controller, Button

from app.logger import logger
from app.services.keyboard_service import KeyboardService
from app.services.mouse_service import MouseService
from app.ultis.constants import MENU_POSITION, PROFILE_NAME, PROXY_HOST_NAME, PROXY_PORT, USERNAME_PROXY, PASSWORD_PROXY
from app.ultis.helper import sleep_random

mouse = Controller()
ACTION_RUN = False


class ChromeService:
    @classmethod
    async def start_actions(cls):
        global ACTION_RUN
        ACTION_RUN = True
        logger.info("Start actions")

    @classmethod
    async def stop_actions(cls):
        global ACTION_RUN
        ACTION_RUN = False
        logger.info("Stop actions")

    @classmethod
    async def open_chrome(cls):
        await sleep_random(min_wait=1, max_wait=4)
        chrome_path = 'firefox'
        command = [chrome_path]
        subprocess.Popen(command, close_fds=True, start_new_session=True)
        await asyncio.sleep(5)
        # await MouseService.click_position(x=775, y=148)
        # await cls.click_blank_page()

    @classmethod
    async def login_chrome__(cls):
        await sleep_random(min_wait=5, max_wait=30)
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
    async def actions_chrome(cls):
        global ACTION_RUN
        idx = 0
        time_to_get_new_ip = 3  # Default
        index_relax = 0
        is_open_web = False
        ###
        while True:
            while ACTION_RUN:
                logger.info(f"Run time {idx}/{time_to_get_new_ip}")
                start_time = time.time()
                if not is_open_web:
                    logger.info("Open web")
                    KeyboardService().input_text('https://khangon.cloud')
                    await sleep_random(min_wait=3, max_wait=5)
                    KeyboardService().enter_press()
                    await sleep_random(min_wait=5, max_wait=10)
                    is_open_web = True
                if idx == time_to_get_new_ip:
                    # Get new IP
                    logger.info("Refresh IP")
                    KeyboardService().ctr_f5()
                    # Reset default value
                    time_to_get_new_ip = random.randint(3, 4)
                    idx = 0
                    index_relax += 1
                    await sleep_random(min_wait=180, max_wait=300)
                # Click random pos and scroll to end
                await sleep_random(min_wait=60, max_wait=70)
                # click_ads = random.choice([True, True])
                # if click_ads:
                #     await MouseService.click_position(520, 450)
                #     await sleep_random(min_wait=8, max_wait=15)
                #     KeyboardService().ctr_w()
                # await sleep_random(min_wait=20, max_wait=30)
                time_to_ran_click = random.randint(15, 20)
                while time_to_ran_click > 0:
                    click_ran_x = random.randint(230, 430)
                    click_ran_y = random.randint(540, 550)
                    # await MouseService.click_position(click_ran_x, click_ran_y)
                    logger.info(f"Click pos {click_ran_x} {click_ran_y}")
                    mouse.position = (click_ran_x, click_ran_y)
                    mouse.scroll(0, -4)
                    random_boolean = random.choice([True, False, False])
                    if random_boolean:
                        mouse.scroll(0, 1)
                    await sleep_random(min_wait=1, max_wait=3)
                    time_to_ran_click -= 1
                # Click new page
                logger.info("Wait to click next page")
                await sleep_random(min_wait=10, max_wait=15)
                # Scroll up menu
                logger.info("Scroll menu")
                sroll = 10
                while sroll > 0:
                    mouse.position = (80, 335)
                    mouse.scroll(0, 5)
                    sroll -= 1
                    await sleep_random(min_wait=1, max_wait=2)
                menu_x, menu_y = MENU_POSITION[random.randint(0, 16)]
                await MouseService.click_position(menu_x, menu_y)
                logger.info(f"Click menu {menu_x} {menu_y}")
                end_time = time.time()
                elapsed_time = end_time - start_time
                logger.info(f"Time to execute {idx} - {elapsed_time}s")
                idx += 1

    @classmethod
    async def open_youtube(cls):
        await sleep_random(min_wait=5, max_wait=30)
        KeyboardService().auto_press_key(Key.f6)
        await asyncio.sleep(2)
        KeyboardService().input_text('https://youtube.com')
        await asyncio.sleep(2)
        KeyboardService().enter_press()
        return True

    @classmethod
    async def open_proxy_veepn(cls):
        # Click popup vpn
        await sleep_random(min_wait=5, max_wait=30)
        await MouseService.click_position(x=616, y=64)
        # Check group
        await cls.select_proxy()
        # Click start
        await asyncio.sleep(4)
        await MouseService.click_position(x=490, y=230)
        await sleep_random(min_wait=10, max_wait=25)
        # Close app
        await cls.click_blank_page()

    @classmethod
    async def open_proxy(cls):
        # Input name
        await sleep_random(min_wait=1, max_wait=3)
        await MouseService.click_position(x=280, y=335)
        KeyboardService().input_text(PROFILE_NAME)
        # Input host
        await sleep_random(min_wait=2, max_wait=4)
        await MouseService.click_position(x=270, y=395)
        KeyboardService().input_text(PROXY_HOST_NAME)
        # Input port
        await sleep_random(min_wait=1, max_wait=3)
        await MouseService.click_position(x=500, y=395)
        KeyboardService().input_text(PROXY_PORT)
        # Input username
        await sleep_random(min_wait=3, max_wait=4)
        await MouseService.click_position(x=280, y=450)
        KeyboardService().input_text(USERNAME_PROXY)
        # Input password
        await sleep_random(min_wait=3, max_wait=4)
        await MouseService.click_position(x=450, y=450)
        KeyboardService().input_text(PASSWORD_PROXY)
        # Click save
        await sleep_random(min_wait=3, max_wait=4)
        await MouseService.click_position(x=520, y=485)


    @classmethod
    async def select_proxy(cls):
        current_group = os.getenv('GROUP')
        # Click open select
        await asyncio.sleep(4)
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
        # Open tab ext
        await sleep_random(min_wait=1, max_wait=3)
        await MouseService.click_position(x=740, y=85)
        # Click no proxy
        await sleep_random(min_wait=1, max_wait=3)
        await MouseService.click_position(x=600, y=125)

    @classmethod
    async def close_chrome(cls):
        await MouseService.click_position(x=791, y=12)

    @classmethod
    async def install(cls):
        await sleep_random(min_wait=2, max_wait=3)
        KeyboardService().new_tab()
        await sleep_random(min_wait=2, max_wait=3)
        # Close old tab
        mouse.position = (160, 40)
        mouse.release(Button.middle)
        await sleep_random(min_wait=2, max_wait=3)
        # Close old tab
        mouse.position = (160, 40)
        mouse.release(Button.middle)
        # Ext install
        url = 'https://addons.mozilla.org/en-US/firefox/addon/iproyal-proxy-manager/'
        KeyboardService().input_text(url)
        await asyncio.sleep(6)
        KeyboardService().enter_press()
        await sleep_random(min_wait=5, max_wait=10)
        await MouseService.click_position(x=430, y=440)

    @classmethod
    async def press_enter(cls):
        KeyboardService().enter_press()

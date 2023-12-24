from pynput.keyboard import Controller, Key


class KeyboardService:
    keyboard = None

    def __init__(self):
        self.keyboard = Controller()

    def auto_press_key(self, key):
        self.keyboard.press(key)
        self.keyboard.release(key)

    def input_text(self, text):
        self.keyboard.type(text)

    def enter_press(self):
        self.keyboard.press(Key.enter)
        self.keyboard.release(Key.enter)

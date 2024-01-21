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

    def press_key(self, key):
        self.keyboard.press(key)

    def release_key(self, key):
        self.keyboard.release(key)

    def ctr_f5(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press(Key.f5)
        self.keyboard.release(Key.f5)
        self.keyboard.release(Key.ctrl)

    def new_tab(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('n')
        self.keyboard.release('n')
        self.keyboard.release(Key.ctrl)

    def ctr_w(self):
        self.keyboard.press(Key.ctrl)
        self.keyboard.press('w')
        self.keyboard.release('w')
        self.keyboard.release(Key.ctrl)

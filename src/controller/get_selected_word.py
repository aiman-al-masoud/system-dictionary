import os
from time import sleep
from typing import Optional
from model.Config import Config
from pynput.keyboard import Controller, Key, KeyCode
import pyperclip


def get_selected_word(config: Config):
    return linux() or fallback()

def linux() -> Optional[str]:

    try:
        return os.popen('xsel').read()
    except:
        return None


def fallback() -> Optional[str]:

    c = Controller()
    c.press(Key.ctrl)
    c.press(KeyCode.from_char('c'))
    sleep(0.2)
    c.release(KeyCode.from_char('c'))
    c.release(Key.ctrl)

    curr_word = pyperclip.paste()
    return curr_word

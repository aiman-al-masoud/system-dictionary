import os
from typing import Optional, Union
from pynput import keyboard
from model.Context import Context
from ui.BrowserWindow import BrowserWindow
from ui.WordWindow import WordWindow


class Controller:

    def __init__(self, context: Context) -> None:
        self.context = context
        self.listener = keyboard.Listener(on_press=self.switch)

    def start(self):
        self.listener.start()

    def switch(self, key: Union[keyboard.KeyCode, keyboard.Key, None]):

        if key == keyboard.Key.ctrl_r:
            self.on_ask_word()

    def on_ask_word(self):

        word = os.popen('xsel').read()
        print(word)
        word_entry = self.context.word_dict[word]

        if word_entry:
            BrowserWindow(word_entry)

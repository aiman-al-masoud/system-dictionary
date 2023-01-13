from typing import Union
from pynput import keyboard
from controller.get_selected_word import get_selected_word
from model.Context import Context
from view.get_window import get_window


class Controller:

    def __init__(self, context: Context) -> None:
        self.context = context
        self.listener = keyboard.Listener(on_press=self.switch)

    def start(self):
        self.listener.start()

    def switch(self, key: Union[keyboard.KeyCode, keyboard.Key, None]):

        if key == keyboard.Key.ctrl_r:
            self.on_lookup_word()

    def on_lookup_word(self):

        dict_entry = self.context.word_dict[get_selected_word()]

        if dict_entry:
            get_window(dict_entry, self.context.config).open()

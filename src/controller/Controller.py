from pynput import keyboard
from controller.KeyListener import KeyListener
from controller.get_selected_word import get_selected_word
from model.Context import Context
from view.get_window import get_window


class Controller:

    def __init__(self, context: Context) -> None:
        self.context = context
        self.key_listener = KeyListener()
        self.key_listener.define_combo({keyboard.Key.ctrl_l.name, keyboard.Key.space.name}, self.on_lookup_word)

    def start(self):
        self.key_listener.start()

    def on_lookup_word(self):

        dict_entry = self.context.word_dict[get_selected_word()]

        if dict_entry:
            get_window(dict_entry, self.context.config).open()

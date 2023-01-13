from time import sleep
from typing import Callable, List
from controller.KeyListener import KeyListener
from controller.get_selected_word import get_selected_word
from model.Context import Context
from view.get_history import get_history
from view.get_window import get_window
import threading


class Controller:

    def __init__(self, context: Context) -> None:
        self.context = context
        self.k_lstnr = KeyListener()
        self.cmd_queue: List[str] = []

        for c in context.config.combos:
            self.k_lstnr.add_combo(
                c.keys, lambda c=c.command: self.add_to_cmd_queue(c))

    def start(self):
        self.k_lstnr.start()
        threading.Thread(target=self.process_events, args=()).start()

    def process_events(self):

        while True:

            for c in self.cmd_queue:
                self.command_to_method(c)()

            self.cmd_queue.clear()

            sleep(0.2)

    def add_to_cmd_queue(self, cmd: str):
        self.cmd_queue.append(cmd)

    def command_to_method(self, cmd: str) -> Callable:

        return {
            'lookup_word': self.lookup_word,
            'show_history': self.show_history
        }[cmd]

    def lookup_word(self):

        selected_word = get_selected_word(self.context.config)

        if not selected_word:
            return

        self.context.history.add(selected_word)

        dict_entry = self.context.word_dict[selected_word]

        if dict_entry:
            get_window(dict_entry, self.context.config).open()

    def show_history(self):

        get_history(self.context).open()

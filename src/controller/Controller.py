from time import sleep
from typing import Callable
from pynput import keyboard
from controller.KeyListener import KeyListener
from controller.get_selected_word import get_selected_word
from model.Command import Command
from model.Context import Context
from view.get_window import get_window
import threading


class Controller:

    def __init__(self, context: Context) -> None:
        self.context = context
        self.k_lstnr = KeyListener()
        self.cmd_queue = []

        for c in context.config.combos:
            self.k_lstnr.add_combo(
                c.keys, lambda: self.add_to_cmd_queue(c.command))

    def start(self):
        self.k_lstnr.start()
        threading.Thread(target=self.process_events, args=()).start()

    def process_events(self):

        while True:

            for c in self.cmd_queue:
                self.command_to_method(c)()

            self.cmd_queue.clear()

            sleep(0.2)

    def add_to_cmd_queue(self, cmd: Command):
        self.cmd_queue.append(cmd)

    def command_to_method(self, cmd: Command) -> Callable:

        return {
            Command.lookup_word: self.lookup_word
        }[cmd]

    def lookup_word(self):

        selected_word = get_selected_word(self.context.config)

        if not selected_word:
            return

        dict_entry = self.context.word_dict[selected_word]

        if dict_entry:
            get_window(dict_entry, self.context.config).open()

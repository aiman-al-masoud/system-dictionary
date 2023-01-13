from enum import Enum
from typing import Callable, FrozenSet, Set, Tuple
from pynput import keyboard


class KeyListener():

    def __init__(self) -> None:
        self.current :Set[Enum] = set()  # currently active keys and modifiers
        self.combinations :Set[Tuple[FrozenSet[Enum], Callable]] = set()

    def start(self):

        keyboard.Listener(on_press=self.on_press,
                          on_release=self.on_release).start()

    def define_combo(self, combo: Set[str], callback: Callable):
        self.combinations.add((frozenset({keyboard.Key._member_map_[k] for k in combo}), callback))

    def on_press(self, key):

        for combo, callback in self.combinations:

            if key in combo:
                self.current.add(key)
                if all(k in self.current for k in combo):
                    callback()

    def on_release(self, key):
        try:
            self.current.remove(key)
        except KeyError:
            pass

from enum import Enum
from typing import Callable, FrozenSet, Set, Tuple, Union
from pynput import keyboard


class KeyListener():

    def __init__(self) -> None:
        # currently active keys and modifiers
        self.current: Set[Union[Enum, keyboard.KeyCode]] = set()
        self.combinations: Set[Tuple[FrozenSet[Union[Enum,
                                                     keyboard.KeyCode]], Callable]] = set()

    def start(self):

        keyboard.Listener(on_press=self.on_press,
                          on_release=self.on_release).start()

    def add_combo(self, combo: Set[str], callback: Callable):
        self.combinations.add((frozenset({self.string_to_key(k) for k in combo}), callback))

    def string_to_key(self, k: str):

        try:
            return keyboard.Key._member_map_[k]
        except:
            return keyboard.KeyCode.from_char(k)

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

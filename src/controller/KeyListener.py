from pynput import keyboard


class KeyListener():

    def __init__(self) -> None:
        self.current = set()  # currently active modifiers
        self.combinations = set()

    def start(self):

        keyboard.Listener(on_press=self.on_press,
                          on_release=self.on_release).start()

    def define_combo(self, combo, callback):
        self.combinations.add((frozenset(combo), callback))

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

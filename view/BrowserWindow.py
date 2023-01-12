import os

from model.DictEntry import DictEntry
from view.WordWindow import WordWindow


class BrowserWindow(WordWindow):

    def __init__(self, dict_entry: DictEntry) -> None:
        self.dict_entry = dict_entry

    def open(self):

        with open('tmp.html', 'w+') as f:

            defs = [m.definition for m in self.dict_entry.meanings]
            f.write(self.dict_entry.word + str(defs))

        os.popen('firefox tmp.html')

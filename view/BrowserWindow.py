import os
from model.Config import Config

from model.DictEntry import DictEntry
from view.WordWindow import WordWindow


class BrowserWindow(WordWindow):

    def __init__(self, dict_entry: DictEntry, config:Config) -> None:
        self.dict_entry = dict_entry
        self.config = config

    def open(self):

        with open(self.config.tmp_file_name, 'w+') as f:

            defs = [m.definition for m in self.dict_entry.meanings]
            f.write(self.dict_entry.word + str(defs))

        os.popen(f'firefox {self.config.tmp_file_name}')

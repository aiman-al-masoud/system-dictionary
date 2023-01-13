import os
from model.Config import Config

from model.DictEntry import DictEntry
from .to_html import to_html
from view.WordWindow import WordWindow


class BrowserWindow(WordWindow):

    def __init__(self, dict_entry: DictEntry, config: Config) -> None:
        self.dict_entry = dict_entry
        self.config = config

    def open(self):

        with open(self.config.tmp_file_name, 'w+') as f:

            f.write(to_html(self.dict_entry))

        os.popen(f'firefox {self.config.tmp_file_name}')

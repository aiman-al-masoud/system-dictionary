import os
from dataclasses import dataclass
from typing import List
import json

from model.Config import Config


@dataclass
class History:

    words: List[str]
    history_file: str

    def add(self, word: str):

        if word in self.words:
            return

        self.words.append(word)

        with open(self.history_file, 'a+') as f:
            f.write(f'{word.strip()}\n')

    @classmethod
    def from_json(cls, json: List[str], history_file: str) -> 'History':
        return History(json, history_file)

    @classmethod
    def get_history(cls, config: Config) -> 'History':

        try:
            word_list = [w.replace('\n', '').strip() for w in open(config.paths.history_file, 'r').readlines()]
        except:
            word_list = []

        return cls.from_json(word_list, config.paths.history_file)

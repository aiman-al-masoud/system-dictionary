import json
import os
import pickle
from typing import Optional
from model.DictEntry import DictEntry
from model.Config import Config


class WordDict(dict):

    def __getitem__(self, __key: str) -> Optional[DictEntry]:
        try:
            return super().__getitem__(__key.lower().strip())
        except:
            return None

    @classmethod
    def from_json(cls, json: dict) -> 'WordDict':

        d = WordDict()

        for w, e in json.items():
            word = w.lower()
            d.update({word: DictEntry.from_json(word, e)})

        return d

    @classmethod
    def from_path(cls, dir: str) -> 'WordDict':

        files = [os.path.join(dir, f) for f in os.listdir(dir)]
        d = WordDict()

        for f_path in files:
            with open(f_path, 'r') as f:
                d.update(cls.from_json(json.loads(f.read())))

        return d

    @classmethod
    def from_pickle(cls, path: str) -> 'WordDict':

        with open(path, 'rb') as f:
            return pickle.load(f)

    def to_pickle(self, path: str):

        with open(path, 'wb+') as f:
            pickle.dump(self, f)

    @classmethod
    def get_word_dict(cls, config: Config):

        try:
            return cls.from_pickle(config.paths.cache_pickle)
        except:
            d = cls.from_path(config.paths.dict_dir)
            d.to_pickle(config.paths.cache_pickle)
            return d

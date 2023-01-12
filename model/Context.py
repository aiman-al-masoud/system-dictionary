import os
from dataclasses import dataclass
from model.Config import Config
from model.WordDict import WordDict


@dataclass
class Context:
    config: Config
    word_dict: WordDict

    @classmethod
    def get_context(cls) -> 'Context':

        path = os.path.join(os.path.split(__file__)[0], '..', 'config', 'config.json')
        config = Config.from_path(path)
        word_dict = WordDict.get_word_dict(config)

        return Context(config, word_dict)

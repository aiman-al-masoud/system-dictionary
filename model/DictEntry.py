from typing import List
from dataclasses import dataclass
from model.Meaning import Meaning


@dataclass
class DictEntry:
    word: str
    meanings: List[Meaning]
    synonyms: List[str]
    antonyms: List[str]

    @classmethod
    def from_json(cls, word: str, json: dict):

        meanings = [Meaning.from_json(v) for m, v in json['MEANINGS'].items()]
        return DictEntry(word, meanings, json['SYNONYMS'], json['ANTONYMS'])
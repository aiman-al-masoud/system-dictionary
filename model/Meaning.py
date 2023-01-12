from typing import Any, List
from model.WordType import WordType
from dataclasses import dataclass


@dataclass
class Meaning:
    word_type: WordType
    definition: str
    tags: List[str]

    @classmethod
    def from_json(cls, json: dict) -> 'Meaning':
        return Meaning(WordType.from_str(json[0]), json[1] or '', json[2:] or [])
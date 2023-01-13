from enum import Enum


class WordType(Enum):
    NOUN = 'NOUN'
    VERB = 'VERB'
    ADJ = 'ADJ'
    ADV = 'ADV'

    @classmethod
    def from_str(cls, val: str) -> 'WordType':
        return {
            'noun': WordType.NOUN,
            'verb': WordType.VERB,
            'adjective': WordType.ADJ,
            'adverb': WordType.ADV
        }[val.lower()]
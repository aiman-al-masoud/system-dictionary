from enum import Enum


class Command(Enum):
    lookup_word = 'lookup_word'

    @classmethod
    def from_string(cls, string: str) -> 'Command':
        return {
            "lookup_word": cls.lookup_word
        }[string.lower()]

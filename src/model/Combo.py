
from dataclasses import dataclass
from typing import FrozenSet, Set

# from controller.Command import Command


@dataclass
class Combo:
    command: str
    keys: Set[str]

    @classmethod
    def from_json(cls, json: dict):

        return Combo(json['command'], set(json['keys']))

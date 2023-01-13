
from dataclasses import dataclass
from typing import FrozenSet, Set

from model.Command import Command


@dataclass
class Combo:
    command: Command
    keys: Set[str]

    @classmethod
    def from_json(cls, json: dict):

        return Combo(Command.from_string(json['command']), set(json['keys']))

from dataclasses import dataclass
import json
from typing import Sequence

from model.Combo import Combo
from model.Paths import Paths


@dataclass
class Config:
    paths: Paths
    combos: Sequence[Combo]

    @classmethod
    def from_json(cls, json: dict, relative_to: str) -> 'Config':

        return Config(Paths.from_json(json['paths'], relative_to),
                      [Combo.from_json(c) for c in json['combos']])

    @classmethod
    def from_path(cls, path: str) -> 'Config':
        return cls.from_json(json.loads(open(path, 'r').read()), path)
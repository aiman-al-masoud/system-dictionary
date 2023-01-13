from dataclasses import dataclass


@dataclass
class Paths:
    dict_dir: str
    cache_pickle: str
    tmp_file_name: str

    @classmethod
    def from_json(cls, json: dict, relative_to: str):
        return Paths(json['dict_dir'], json['cache_pickle'], json['tmp_file_name'])
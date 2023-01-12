from dataclasses import dataclass
import json
import os


@dataclass
class Config:
    dict_dir: str
    cache_pickle: str
    tmp_file_name: str

    @classmethod
    def from_json(cls, json: dict) -> 'Config':
        return Config(json['dict_dir'], json['cache_pickle'], json['tmp_file_name'])

    @classmethod
    def from_path(cls, path: str) -> 'Config':

        def rltvz(p: str):
            config_dir = os.path.split(path)[0]
            return os.path.join(config_dir, *p.split('/'))

        myjson = json.loads(open(path).read())
        return Config(rltvz(myjson['dict_dir']), rltvz(myjson['cache_pickle']), rltvz(myjson['tmp_file_name']))

import os

from model.DictEntry import DictEntry


class BrowserWindow:

    def __init__(self, dict_entry:DictEntry) -> None:

        with open('tmp.html', 'w+') as f:

            defs = [m.definition for m in dict_entry.meanings]
            f.write(dict_entry.word + str(defs))

        os.popen('firefox tmp.html')

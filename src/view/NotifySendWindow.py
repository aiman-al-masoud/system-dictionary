import os
from functools import reduce
from model.DictEntry import DictEntry
from view.WordWindow import WordWindow


class NotifySendWindow(WordWindow):

    def __init__(self, dict_entry: DictEntry) -> None:
        self.dict_entry = dict_entry

    def open(self):

        word = self.dict_entry.word
        defs = reduce(lambda a, b: a+' / '+b, [m.definition for m in self.dict_entry.meanings], '')
        os.popen(f'notify-send "{word}" "{defs}"')

from model.DictEntry import DictEntry
from view.BrowserWindow import BrowserWindow
from view.WordWindow import WordWindow


def get_window(dict_entry: DictEntry)->WordWindow:
    return BrowserWindow(dict_entry)



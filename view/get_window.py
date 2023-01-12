from model.Config import Config
from model.DictEntry import DictEntry
from view.BrowserWindow import BrowserWindow
from view.WordWindow import WordWindow


def get_window(dict_entry: DictEntry, config:Config)->WordWindow:
    return BrowserWindow(dict_entry, config)



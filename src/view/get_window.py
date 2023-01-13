from model.Config import Config
from model.DictEntry import DictEntry
from view.BrowserWindow import BrowserWindow
from view.NotifySendWindow import NotifySendWindow
from view.WordWindow import WordWindow


def get_window(dict_entry: DictEntry, config: Config) -> WordWindow:

    if config.operatin_system == 'Linux':
        return NotifySendWindow(dict_entry)
    else:
        return BrowserWindow(dict_entry, config)

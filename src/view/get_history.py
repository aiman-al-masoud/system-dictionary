from view.HistoryOnBrowser import HistoryOnBrowser
from view.HistoryView import HistoryView

from model.Context import Context


def get_history(context: Context) -> HistoryView:
    return HistoryOnBrowser(context)

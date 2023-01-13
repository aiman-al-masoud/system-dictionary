from model.Config import Config
from model.Context import Context
from view.HistoryView import HistoryView
from model.History import History
import webbrowser


class HistoryOnBrowser(HistoryView):

    def __init__(self, context: Context) -> None:
        super().__init__()
        self.context = context

    def open(self):

        with open(self.context.config.paths.tmp_file_name, 'w+') as f:
            f.write(str(self.context.history.words))

        webbrowser.open(self.context.config.paths.tmp_file_name)

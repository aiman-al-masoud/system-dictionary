from model.Context import Context
from view.HistoryView import HistoryView
import webbrowser
from functools import reduce


class HistoryOnBrowser(HistoryView):

    def __init__(self, context: Context) -> None:
        super().__init__()
        self.context = context

    def open(self):

        with open(self.context.config.paths.tmp_file_name, 'w+') as f:

            html = '<ul>' +  \
                reduce(lambda a, b: a+b, [f'<li>{w}</li>' for w in self.context.history.words], '') +\
                '</ul>'

            f.write(html)

        webbrowser.open(self.context.config.paths.tmp_file_name)

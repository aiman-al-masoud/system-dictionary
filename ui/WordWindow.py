import tkinter as tk

from model.DictEntry import DictEntry


class WordWindow(tk.Tk):

    def __init__(self, entry: DictEntry) -> None:
        super()
        tk.Label(text=entry.word).pack()
        tk.mainloop()
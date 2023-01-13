import os

def get_selected_word():
    return os.popen('xsel').read()
    
import os

from model.Config import Config

def get_selected_word(config:Config):
    return os.popen('xsel').read()
    
#!/bin/python3
from model.Context import Context
from controller.Controller import Controller

context = Context.get_context()
controller = Controller(context)
controller.start()

while True:
    pass

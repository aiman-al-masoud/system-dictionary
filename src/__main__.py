#!/bin/python3
from model.Context import Context
from controller.Controller import Controller

context = Context.get_context()

# print(context.config)
controller = Controller(context)
controller.start()

while True:
    pass

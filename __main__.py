
from model.Context import Context
from controller.Controller import Controller

context  = Context.get_context()

controller = Controller(context)

controller.start()

while True:
    pass

# print(context.word_dict['dog'])
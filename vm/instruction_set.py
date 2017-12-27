import logging

class Set_Instruction(object):

    def __init__(self, register, value):
        logging.debug("Creating SET")

        self.register = register
        self.value = value

    def execute(self, vm_state):
        logging.debug("Executing SET")

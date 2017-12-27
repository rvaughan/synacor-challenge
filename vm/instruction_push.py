import logging

class Push_Instruction(object):

    def __init__(self, value):
        logging.debug("Creating PSH")

        self.value = value

    def execute(self, memory, registers):
        logging.debug("Executing PSH")

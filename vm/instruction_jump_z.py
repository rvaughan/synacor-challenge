import logging

class JZ_Instruction(object):

    def __init__(self, location, value):
        logging.debug("Creating JZ")

        self.location = location
        self.value = value

    def execute(self, memory, registers):
        logging.debug("Executing JZ")

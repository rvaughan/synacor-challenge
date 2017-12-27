import logging

class Not_Instruction(object):

    def __init__(self, location, value):
        logging.debug("Creating NOT")

        self.location = location
        self.value = value

    def execute(self, memory, registers):
        logging.debug("Executing NOT")

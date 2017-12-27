import logging

class RMem_Instruction(object):

    def __init__(self, location, value):
        logging.debug("Creating RMEM")

        self.location = location
        self.value = value

    def execute(self, memory, registers):
        logging.debug("Executing RMEM")

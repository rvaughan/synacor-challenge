import logging

class WMem_Instruction(object):

    def __init__(self, location, value):
        logging.debug("Creating WMEM")

        self.location = location
        self.value = value

    def execute(self, memory, registers):
        logging.debug("Executing WMEM")

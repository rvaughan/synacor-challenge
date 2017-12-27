import logging

class In_Instruction(object):

    def __init__(self, location):
        logging.debug("Creating IN")

        self.location = location

    def execute(self, memory, registers):
        logging.debug("Executing IN")

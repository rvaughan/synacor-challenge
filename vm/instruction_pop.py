import logging

class Pop_Instruction(object):

    def __init__(self, location):
        logging.debug("Creating POP")

        self.location = location

    def execute(self, memory, registers):
        logging.debug("Executing POP")

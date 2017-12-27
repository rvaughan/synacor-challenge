import logging

class Jump_Instruction(object):

    def __init__(self, location):
        logging.debug("Creating JMP")

        self.location = location

    def execute(self, memory, registers):
        logging.debug("Executing JMP")

import logging

class Halt_Instruction(object):

    def __init__(self):
        logging.debug("Creating HALT")

    def execute(self, memory, registers):
        logging.info("Execution HALT'd")
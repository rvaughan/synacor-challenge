import logging

class NOOP_Instruction(object):

    def __init__(self):
        logging.debug("Creating NOOP")

    def execute(self, memory, registers):
        logging.info("Executing NOOP")

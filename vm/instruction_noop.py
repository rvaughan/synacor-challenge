import logging

class NOOP_Instruction(object):

    def __init__(self):
        logging.debug("Creating NOOP")

    def execute(self, vm_state):
        logging.info("Executing NOOP")

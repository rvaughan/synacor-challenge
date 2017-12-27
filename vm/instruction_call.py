import logging

class Call_Instruction(object):

    def __init__(self, location):
        logging.debug("Creating CALL")

        self.location = location

    def execute(self, vm_state):
        logging.debug("Executing CALL")

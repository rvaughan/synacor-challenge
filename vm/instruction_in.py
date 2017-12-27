import logging

class In_Instruction(object):

    def __init__(self, location):
        logging.debug("Creating IN")

        self.location = location

    def execute(self, vm_state):
        logging.debug("Executing IN")

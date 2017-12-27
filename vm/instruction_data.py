import logging

class Data_Instruction(object):

    def __init__(self):
        logging.debug("Creating DATA")

    def execute(self, vm_state):
        logging.debug("Executing DATA")

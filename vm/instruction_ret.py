import logging

class Ret_Instruction(object):

    def __init__(self):
        logging.debug("Creating RET")

    def execute(self, vm_state):
        logging.debug("Executing RET")

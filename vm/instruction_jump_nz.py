import logging

class JNZ_Instruction(object):

    def __init__(self, location, value_a):
        logging.debug("Creating JNZ")

        self.location = location
        self.value_a = value_a

    def execute(self, vm_state):
        logging.debug("Executing JNZ")

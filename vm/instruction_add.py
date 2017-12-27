import logging

class Add_Instruction(object):

    def __init__(self, location, value_a, value_b):
        logging.debug("Creating ADD")

        self.location = location
        self.value_a = value_a
        self.value_b = value_b

    def execute(self, vm_state):
        logging.debug("Executing ADD")

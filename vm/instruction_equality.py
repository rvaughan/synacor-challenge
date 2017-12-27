import logging

class Equality_Instruction(object):

    def __init__(self, location, value_a, value_b):
        logging.debug("Creating EQ")

        self.location = location
        self.value_a = value_a
        self.value_b = value_b

    def execute(self, memory, registers):
        logging.debug("Executing EQ")

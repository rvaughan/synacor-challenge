import logging

from instruction import Instruction


class Multiply_Instruction(Instruction):

    def __init__(self, location, value_a, value_b):
        logging.debug("Creating MULT")

        self.location = location
        self.value_a = value_a
        self.value_b = value_b

    def dump(self):
        print "MUL {0} {1} {2}".format(self.location, self.value_a, self.value_b)

    def execute(self, vm_state):
        logging.debug("Executing MULT")

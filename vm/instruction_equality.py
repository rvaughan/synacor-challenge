import logging

from instruction import Instruction


class Equality_Instruction(Instruction):

    def __init__(self, location, value_a, value_b):
        logging.debug("Creating EQ")

        self.location = location
        self.value_a = value_a
        self.value_b = value_b

    def dump(self, vm_state):
        print "[{:04X}] EQ {:0} {:0} {:0}".format(vm_state["instruction_pointer"]-4,self.location, self.value_a, self.value_b)

    def execute(self, vm_state):
        logging.debug("Executing EQ")

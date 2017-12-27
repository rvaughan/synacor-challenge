import logging

from instruction import Instruction


class RMem_Instruction(Instruction):

    def __init__(self, location, value):
        logging.debug("Creating RMEM")

        self.location = location
        self.value = value

    def dump(self, vm_state):
        print "[{:04X}] RMEM {:0} {:0}".format(vm_state["instruction_pointer"]-3, self.location, self.value)

    def execute(self, vm_state):
        logging.debug("Executing RMEM")

import logging

from instruction import Instruction


class WMem_Instruction(Instruction):

    def __init__(self, location, value):
        logging.debug("Creating WMEM")

        self.location = location
        self.value = value

    def dump(self, vm_state):
        print "[{:04X}] WMEM {:0} {:0}".format(vm_state["instruction_pointer"]-3, self.location, self.value)

    def execute(self, vm_state):
        logging.debug("Executing WMEM")

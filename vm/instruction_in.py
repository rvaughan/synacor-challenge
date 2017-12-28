import logging

from instruction import Instruction


class In_Instruction(Instruction):

    def __init__(self, location):
        logging.debug("Creating IN")

        self.location = location

    def dump(self, vm_state):
        return "[{:04X}] IN {:0}".format(vm_state["instruction_pointer"]-2, self.location)

    def execute(self, vm_state):
        logging.debug("Executing IN")

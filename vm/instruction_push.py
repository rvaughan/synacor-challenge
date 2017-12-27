import logging

from instruction import Instruction


class Push_Instruction(Instruction):

    def __init__(self, value):
        logging.debug("Creating PSH")

        self.value = value

    def dump(self, vm_state):
        print "[{:04X}] PSH {:0}".format(vm_state["instruction_pointer"]-2, self.value)

    def execute(self, vm_state):
        logging.debug("Executing PSH")

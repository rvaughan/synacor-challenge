import logging

from instruction import Instruction


class Ret_Instruction(Instruction):

    def __init__(self, location):
        logging.debug("Creating RET")
        self.location = location

    def dump(self, vm_state):
        print "[{:04X}] RET".format(vm_state["instruction_pointer"]-2)

    def execute(self, vm_state):
        logging.debug("Executing RET")

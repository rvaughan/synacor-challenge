import logging

from instruction import Instruction


class Ret_Instruction(Instruction):

    def __init__(self):
        logging.debug("Creating RET")

    def dump(self, vm_state):
        print "[{:04X}] RET".format(vm_state["instruction_pointer"])

    def execute(self, vm_state):
        logging.debug("Executing RET")

import logging

from instruction import Instruction


class Halt_Instruction(Instruction):

    def __init__(self):
        logging.debug("Creating HALT")

    def dump(self, vm_state):
        print "[{:04}] HALT".format(vm_state["instruction_pointer"])

    def execute(self, vm_state):
        logging.info("Execution HALT'd")

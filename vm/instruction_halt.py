import logging

from instruction import Instruction


class Halt_Instruction(Instruction):

    def __init__(self):
        logging.debug("Creating HALT")

    def dump(self):
        print "HALT"

    def execute(self, vm_state):
        logging.info("Execution HALT'd")

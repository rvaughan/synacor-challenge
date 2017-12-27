import logging

from instruction import Instruction


class Ret_Instruction(Instruction):

    def __init__(self):
        logging.debug("Creating RET")

    def dump(self):
        print "RET"

    def execute(self, vm_state):
        logging.debug("Executing RET")

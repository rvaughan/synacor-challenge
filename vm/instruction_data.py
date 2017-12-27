import logging

from instruction import Instruction


class Data_Instruction(Instruction):

    def __init__(self):
        logging.debug("Creating DATA")

    def execute(self, vm_state):
        logging.debug("Executing DATA")

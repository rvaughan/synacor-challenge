import logging

from instruction import Instruction


class Not_Instruction(Instruction):

    def __init__(self, location, value):
        logging.debug("Creating NOT")

        self.location = location
        self.value = value

    def execute(self, vm_state):
        logging.debug("Executing NOT")

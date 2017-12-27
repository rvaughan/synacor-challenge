import logging

from instruction import Instruction


class Call_Instruction(Instruction):

    def __init__(self, location):
        logging.debug("Creating CALL")

        self.location = location

    def execute(self, vm_state):
        logging.debug("Executing CALL")

import logging

from instruction import Instruction


class Pop_Instruction(Instruction):

    def __init__(self, location):
        logging.debug("Creating POP")

        self.location = location

    def execute(self, vm_state):
        logging.debug("Executing POP")

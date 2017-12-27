import logging

from instruction import Instruction


class WMem_Instruction(Instruction):

    def __init__(self, location, value):
        logging.debug("Creating WMEM")

        self.location = location
        self.value = value

    def execute(self, vm_state):
        logging.debug("Executing WMEM")

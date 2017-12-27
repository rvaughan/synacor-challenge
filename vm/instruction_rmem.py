import logging

from instruction import Instruction


class RMem_Instruction(Instruction):

    def __init__(self, location, value):
        logging.debug("Creating RMEM")

        self.location = location
        self.value = value

    def dump(self):
        print "RMEM {0} {1}".format(self.location, self.value)

    def execute(self, vm_state):
        logging.debug("Executing RMEM")

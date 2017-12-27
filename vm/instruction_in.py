import logging

from instruction import Instruction


class In_Instruction(Instruction):

    def __init__(self, location):
        logging.debug("Creating IN")

        self.location = location

    def dump(self):
        print "IN {0}".format(self.location)

    def execute(self, vm_state):
        logging.debug("Executing IN")

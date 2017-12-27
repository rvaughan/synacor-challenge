import logging

from instruction import Instruction


class JZ_Instruction(Instruction):

    def __init__(self, value, location):
        logging.debug("Creating JZ")

        self.value = value
        self.location = location

    def dump(self):
        print "JZ {0} {1}".format(self.location, self.value)

    def execute(self, vm_state):
        value = self._get_value(vm_state, self.value)
        if value == 0:
            vm_state["instruction_pointer"] = self.value

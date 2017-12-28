import logging

from instruction import Instruction


class Not_Instruction(Instruction):

    def __init__(self, location, value):
        self.location = location
        self.value = value

    def dump(self, vm_state):
        print "[{:04X}] NOT {:0} {:0}".format(vm_state["instruction_pointer"]-3, self.location, self.value)

    def execute(self, vm_state):
        value = self._get_value(vm_state, self.value)

        # Need to remember that the values stored must be 15 bit only, so
        # we need to mask off the 16th bit...
        self._set_value(vm_state, self.location, (~value & ((1 << 15) - 1)))

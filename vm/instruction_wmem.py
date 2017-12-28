import logging

from instruction import Instruction


class WMem_Instruction(Instruction):

    def __init__(self, location, value):
        self.location = location
        self.value = value

    def dump(self, vm_state):
        return "[{:04X}] WMEM {:0} {:0}".format(vm_state["instruction_pointer"]-3, self.location, self.value)

    def execute(self, vm_state):
        mem_loc = self._get_value(vm_state, self.location)
        value = self._get_value(vm_state, self.value)
        vm_state["memory"][mem_loc] = value

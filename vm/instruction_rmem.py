import logging

from instruction import Instruction


class RMem_Instruction(Instruction):

    def __init__(self, location, value):
        self.location = location
        self.value = value

    def dump(self, vm_state):
        return "[{:04X}] RMEM {:0} {:0}".format(vm_state["instruction_pointer"]-3, self.location, self.value)

    def execute(self, vm_state):
        mem_location = self._get_value(vm_state, self.value)

        self._set_value(vm_state, self.location, vm_state["memory"][mem_location])

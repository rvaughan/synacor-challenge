import logging

from instruction import Instruction


class Push_Instruction(Instruction):

    def __init__(self, value):
        self.value = value

    def dump(self, vm_state):
        return "[{:04X}] PSH {:0}".format(vm_state["instruction_pointer"]-2, self.value)

    def execute(self, vm_state):
        value = self._get_value(vm_state, self.value)
        vm_state["stack"].append(value)

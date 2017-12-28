import logging

from instruction import Instruction


class Set_Instruction(Instruction):

    def __init__(self, register, value):
        self.register = register
        self.value = value

    def dump(self, vm_state):
        return "[{:04X}] SET {:0} {:0}".format(vm_state["instruction_pointer"]-3, self.register, self.value)

    def execute(self, vm_state):
        self._set_value(vm_state, self.register, self.value)

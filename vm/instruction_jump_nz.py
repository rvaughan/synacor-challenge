import logging

from instruction import Instruction


class JNZ_Instruction(Instruction):

    def __init__(self, value, location):
        self.value = value
        self.location = location

    def execute(self, vm_state):
        value = self._get_value(vm_state, self.value)
        if value != 0:
            vm_state["instruction_pointer"] = self.value

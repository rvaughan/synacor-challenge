import logging

from instruction import Instruction


class Pop_Instruction(Instruction):

    def __init__(self, location):
        self.location = location

    def dump(self, vm_state):
        return "[{:04X}] POP {:0}".format(vm_state["instruction_pointer"]-2, self.location)

    def execute(self, vm_state):
        value = vm_state["stack"].pop()
        self._set_value(vm_state, self.location, value)

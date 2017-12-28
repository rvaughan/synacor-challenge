import logging

from instruction import Instruction


class Call_Instruction(Instruction):

    def __init__(self, location):
        self.location = location

    def dump(self, vm_state):
        print "[{:04X}] CALL {:04X}".format(vm_state["instruction_pointer"]-2, self.location)

    def execute(self, vm_state):
        vm_state["stack"].append(vm_state["instruction_pointer"])
        vm_state["instruction_pointer"] = self._get_value(vm_state, self.location)

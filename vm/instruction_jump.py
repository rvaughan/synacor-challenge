import logging

from instruction import Instruction


class Jump_Instruction(Instruction):

    def __init__(self, location):
        self.location = location

    def dump(self, vm_state):
        print "[{:04X}] JMP {:0}".format(vm_state["instruction_pointer"], self.location)

    def execute(self, vm_state):
        vm_state["instruction_pointer"] = self.location

import logging

from instruction import Instruction


class Data_Instruction(Instruction):

    def __init__(self, data):
        self.data = data

    def dump(self, vm_state):
        print "[{:04X}] DATA {:0}".format(vm_state["instruction_pointer"]-1, self.data)

    def execute(self, vm_state):
        pass

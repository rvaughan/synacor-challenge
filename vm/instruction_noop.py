import logging

from instruction import Instruction


class NOOP_Instruction(Instruction):

    def __init__(self):
        pass

    def dump(self, vm_state):
        print "[{:04X}] NOP".format(vm_state["instruction_pointer"]-1)

    def execute(self, vm_state):
        pass

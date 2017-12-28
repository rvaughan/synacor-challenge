import logging

from instruction import Instruction


class Ret_Instruction(Instruction):

    def __init__(self):
        pass

    def dump(self, vm_state):
        print "[{:04X}] RET".format(vm_state["instruction_pointer"]-1)

    def execute(self, vm_state):
        vm_state["instruction_pointer"] = vm_state["stack"].pop()

import logging

from instruction import Instruction


class NOOP_Instruction(Instruction):

    def __init__(self):
        pass

    def execute(self, vm_state):
        pass

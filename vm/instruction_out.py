import sys

from instruction import Instruction


class Out_Instruction(Instruction):

    def __init__(self, location):
        self.location = location

    def execute(self, vm_state):
        sys.stdout.write(chr(self.location))

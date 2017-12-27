import sys

from instruction import Instruction


class Out_Instruction(Instruction):

    def __init__(self, location):
        self.location = location

    def dump(self, vm_state):
        print "[{:04X}] OUT {:0}".format(vm_state["instruction_pointer"], self.location)

    def execute(self, vm_state):
        if self.location < 256:
            sys.stdout.write(chr(self.location))
        else:
            sys.stdout.write(chr(self._get_value(vm_state, self.location)))

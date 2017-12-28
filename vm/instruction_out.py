import sys

from instruction import Instruction


class Out_Instruction(Instruction):

    def __init__(self, location):
        self.location = location

    def _get_char(self, vm_state):
        result = None

        if self.location < 256:
            result = self.location
        else:
            result = self._get_value(vm_state, self.location)

        if result == 10:
            return '\\n'
        else:
            try:
                return chr(result)
            except ValueError:
                return '*'

    def dump(self, vm_state):
        print "[{:04X}] OUT {:0} '{}'".format(vm_state["instruction_pointer"]-2, self.location, self._get_char(vm_state))

    def execute(self, vm_state):
        sys.stdout.write(self._get_char(vm_state))

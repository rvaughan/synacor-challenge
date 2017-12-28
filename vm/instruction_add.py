import logging

from instruction import Instruction


class Add_Instruction(Instruction):

    def __init__(self, location, value_a, value_b):
        self.location = location
        self.value_a = value_a
        self.value_b = value_b

    def dump(self, vm_state):
        print "[{:04X}] ADD {:0} {:0} {:0}".format(vm_state["instruction_pointer"]-4, self.location, self.value_a, self.value_b)

    def execute(self, vm_state):
        val_a = self._get_value(vm_state, self.value_a)
        val_b = self._get_value(vm_state, self.value_b)

        result = (val_a + val_b) % 32768

        self._set_value(vm_state, self.location, result)

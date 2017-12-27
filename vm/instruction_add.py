import logging

from instruction import Instruction


class Add_Instruction(Instruction):

    def __init__(self, location, value_a, value_b):
        logging.debug("Creating ADD")

        self.location = location
        self.value_a = value_a
        self.value_b = value_b

    def execute(self, vm_state):
        val_a = self._get_value(vm_state, self.value_a)
        val_b = self._get_value(vm_state, self.value_b)

        result = val_a + val_b

        self._set_value(vm_state, self.location, result)

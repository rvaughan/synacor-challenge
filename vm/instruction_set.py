import logging

from instruction import Instruction


class Set_Instruction(Instruction):

    def __init__(self, register, value):
        logging.debug("Creating SET")

        self.register = register
        self.value = value

    def dump(self, vm_state):
        print "[{:04X}] SET {:0} {:0}".format(vm_state["instruction_pointer"], self.register, self.value)

    def execute(self, vm_state):
        logging.debug("Executing SET")

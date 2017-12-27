import logging

from instruction import Instruction


class Data_Instruction(Instruction):

    def __init__(self, data):
        self.data = data

    def dump(self):
        print "DATA {0}".format(self.data)

    def execute(self, vm_state):
        pass

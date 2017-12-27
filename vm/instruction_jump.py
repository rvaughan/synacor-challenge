import logging

class Jump_Instruction(object):

    def __init__(self, location):
        self.location = location

    def execute(self, vm_state):
        vm_state["instruction_pointer"] = self.location

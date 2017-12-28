"""
This module contains the implementation for the IN instruction.

The way this instruction is used is a little odd. It seems as though the VM
code constantly polls the instruction waiting for a newline character. This
means that the input needs to be temporarily stored and pushed into the
specified location one character at a time.
"""
from instruction import Instruction


class In_Instruction(Instruction):

    def __init__(self, location):
        self.location = location

    def dump(self, vm_state):
        return "[{:04X}] IN {:0}".format(vm_state["instruction_pointer"]-2, self.location)

    def execute(self, vm_state):
        # Is there any temporarily stored data from the user already?
        if vm_state["user_input"] is None:
            command = raw_input()

            vm_state["user_input"] = (c for c in command)

        # Return the user input character by character, ensuring that we
        # end with a newline.
        try:
            char = vm_state["user_input"].next()
        except StopIteration:
            # We've read all of the input so reset the temporary variable.
            vm_state["user_input"] = None
            char = '\n'

        self._set_value(vm_state, self.location, ord(char))

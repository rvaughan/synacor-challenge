import sys

class Out_Instruction(object):

    def __init__(self, ascii_char):
        self.ascii_char = ascii_char

    def execute(self, memory, registers):
        sys.stdout.write(chr(self.ascii_char))

import logging

class Out_Instruction(object):

    def __init__(self, location):
        # logging.debug("Creating OUT")

        self.location = location

    def execute(self, memory, registers):
        print self._read_location(memory)

    def _read_location(self, memory):
        pos = self.location
        value = memory[pos]
        pos += 1
        value = (memory[pos] * 256) + value

        return value

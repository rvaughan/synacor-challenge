"""
This module represents the Virtual Machine.
"""
from collections import defaultdict
import logging

from instruction_add import Add_Instruction
from instruction_and import And_Instruction
from instruction_call import Call_Instruction
from instruction_equality import Equality_Instruction
from instruction_greater import Greater_Instruction
from instruction_halt import Halt_Instruction
from instruction_in import In_Instruction
from instruction_jump_nz import JNZ_Instruction
from instruction_jump_z import JZ_Instruction
from instruction_jump import Jump_Instruction
from instruction_mod import Mod_Instruction
from instruction_multiply import Multiply_Instruction
from instruction_noop import NOOP_Instruction
from instruction_not import Not_Instruction
from instruction_or import Or_Instruction
from instruction_out import Out_Instruction
from instruction_push import Push_Instruction
from instruction_pop import Pop_Instruction
from instruction_ret import Ret_Instruction
from instruction_rmem import RMem_Instruction
from instruction_set import Set_Instruction
from instruction_wmem import WMem_Instruction


class VM(object):
    """
    This class represents the Virtual Machine.
    """

    def __init__(self, memory_file):
        """
        Constructor

        memory_file - is the filename of the VM memory data.
        """
        self.current_instruction = None
        self.instruction_pointer = 0
        self.halted = True

        with open(memory_file, "rb") as f:
            self.memory = bytearray(f.read())

        self.registers = defaultdict(int)

        self.stack = []


    def _get_next_instruction(self):
        """
        Processes the memory location as if it were an instruction
        """
        if self.instruction_pointer < len(self.memory):
            self.instruction_pointer, instruction = self._read_location(self.instruction_pointer)

            if instruction == 0:
                self.halted = True
                return Halt_Instruction()
            elif instruction == 1:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value = self._read_location(self.instruction_pointer)
                return Set_Instruction(location, value)
            elif instruction == 2:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                return Push_Instruction(location)
            elif instruction == 3:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                return Pop_Instruction(location)
            elif instruction == 4:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_a = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_b = self._read_location(self.instruction_pointer)
                return Equality_Instruction(location, value_a, value_b)
            elif instruction == 5:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_a = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_b = self._read_location(self.instruction_pointer)
                return Greater_Instruction(location, value_a, value_b)
            elif instruction == 6:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                return Jump_Instruction(location)
            elif instruction == 7:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value = self._read_location(self.instruction_pointer)
                return JNZ_Instruction(location, value)
            elif instruction == 8:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value = self._read_location(self.instruction_pointer)
                return JZ_Instruction(location, value)
            elif instruction == 9:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_a = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_b = self._read_location(self.instruction_pointer)
                return Add_Instruction(location, value_a, value_b)
            elif instruction == 10:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_a = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_b = self._read_location(self.instruction_pointer)
                return Multiply_Instruction(location, value_a, value_b)
            elif instruction == 11:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_a = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_b = self._read_location(self.instruction_pointer)
                return Mod_Instruction(location, value_a, value_b)
            elif instruction == 12:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_a = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_b = self._read_location(self.instruction_pointer)
                return And_Instruction(location, value_a, value_b)
            elif instruction == 13:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_a = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value_b = self._read_location(self.instruction_pointer)
                return Or_Instruction(location, value_a, value_b)
            elif instruction == 14:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value = self._read_location(self.instruction_pointer)
                return Not_Instruction(location, value)
            elif instruction == 15:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value = self._read_location(self.instruction_pointer)
                return RMem_Instruction(location, value)
            elif instruction == 16:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                self.instruction_pointer, value = self._read_location(self.instruction_pointer)
                return WMem_Instruction(location, value)
            elif instruction == 17:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                return Call_Instruction(location)
            elif instruction == 18:
                return Ret_Instruction()
            elif instruction == 19:
                self.instruction_pointer, ascii_char = self._read_location(self.instruction_pointer)
                return Out_Instruction(ascii_char)
            elif instruction == 20:
                self.instruction_pointer, location = self._read_location(self.instruction_pointer)
                return In_Instruction(location)
            elif instruction == 21:
                return NOOP_Instruction()
            else:
                # It's probably just a block of memory...
                logging.warn("Can't execute this instruction. {0}".format(instruction))
                self.halted = True
                return None

    def _read_location(self, start_pos):
        pos = start_pos
        location = self.memory[pos]
        pos += 1
        location = (self.memory[pos] * 256) + location

        return pos + 1, location

    def run(self, start_instruction=0):
        """
        Runs the virtual machine, starting from the specified instruction
        pointer position.
        """
        self.instruction_pointer = start_instruction * 2

        self.halted = False
        while not self.halted:
            self._execute_instruction()

    def _execute_instruction(self):
        self.current_instruction = self._get_next_instruction()

        if self.current_instruction != None:
            self.current_instruction.execute(self.memory, self.registers)

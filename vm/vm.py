"""
This module represents the Virtual Machine.
"""
from collections import defaultdict
import logging
import struct

from instruction_add import Add_Instruction
from instruction_and import And_Instruction
from instruction_call import Call_Instruction
from instruction_data import Data_Instruction
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
        self.state = {}
        self.state["instruction_pointer"] = 0
        self.state["memory"] = []
        self.halted = True
        self.end_of_program = False

        with open(memory_file, "rb") as f:
            chunk = f.read(2)
            while chunk != '':
                self.state["memory"].append(struct.unpack('<H', chunk)[0])
                chunk = f.read(2)

        self.state["registers"] = defaultdict(int)

        self.state["stack"] = []

    def dump(self, start_instruction=0):
        """
        """
        self.state["instruction_pointer"] = start_instruction

        while not self.end_of_program:
            self._dump_instruction()

    def _dump_instruction(self):
        instruction = self._get_next_instruction()

        if instruction != None:
            instruction.dump(self.state)

    def _get_next_instruction(self):
        """
        Processes the memory location as if it were an instruction
        """
        if self.state["instruction_pointer"] < len(self.state["memory"]):
            instruction = self._read_location()

            if instruction == 0:
                self.halted = True
                return Halt_Instruction()
            elif instruction == 1:
                location = self._read_location()
                value = self._read_location()
                return Set_Instruction(location, value)
            elif instruction == 2:
                location = self._read_location()
                return Push_Instruction(location)
            elif instruction == 3:
                location = self._read_location()
                return Pop_Instruction(location)
            elif instruction == 4:
                location = self._read_location()
                value_a = self._read_location()
                value_b = self._read_location()
                return Equality_Instruction(location, value_a, value_b)
            elif instruction == 5:
                location = self._read_location()
                value_a = self._read_location()
                value_b = self._read_location()
                return Greater_Instruction(location, value_a, value_b)
            elif instruction == 6:
                location = self._read_location()
                return Jump_Instruction(location)
            elif instruction == 7:
                value = self._read_location()
                location = self._read_location()
                return JNZ_Instruction(value, location)
            elif instruction == 8:
                value = self._read_location()
                location = self._read_location()
                return JZ_Instruction(value, location)
            elif instruction == 9:
                location = self._read_location()
                value_a = self._read_location()
                value_b = self._read_location()
                return Add_Instruction(location, value_a, value_b)
            elif instruction == 10:
                location = self._read_location()
                value_a = self._read_location()
                value_b = self._read_location()
                return Multiply_Instruction(location, value_a, value_b)
            elif instruction == 11:
                location = self._read_location()
                value_a = self._read_location()
                value_b = self._read_location()
                return Mod_Instruction(location, value_a, value_b)
            elif instruction == 12:
                location = self._read_location()
                value_a = self._read_location()
                value_b = self._read_location()
                return And_Instruction(location, value_a, value_b)
            elif instruction == 13:
                location = self._read_location()
                value_a = self._read_location()
                value_b = self._read_location()
                return Or_Instruction(location, value_a, value_b)
            elif instruction == 14:
                location = self._read_location()
                value = self._read_location()
                return Not_Instruction(location, value)
            elif instruction == 15:
                location = self._read_location()
                value = self._read_location()
                return RMem_Instruction(location, value)
            elif instruction == 16:
                location = self._read_location()
                value = self._read_location()
                return WMem_Instruction(location, value)
            elif instruction == 17:
                location = self._read_location()
                return Call_Instruction(location)
            elif instruction == 18:
                location = self._read_location()
                return Ret_Instruction(location)
            elif instruction == 19:
                location = self._read_location()
                return Out_Instruction(location)
            elif instruction == 20:
                location = self._read_location()
                return In_Instruction(location)
            elif instruction == 21:
                return NOOP_Instruction()
            else:
                # It's probably just a block of memory...
                self.halted = True
                return Data_Instruction(instruction)
        else:
            self.end_of_program = True

    def _read_location(self):
        location = self.state["memory"][self.state["instruction_pointer"]]

        self.state["instruction_pointer"] += 1

        return location

    def run(self, start_instruction=0):
        """
        Runs the virtual machine, starting from the specified instruction
        pointer position.
        """
        self.state["instruction_pointer"] = start_instruction

        self.halted = False
        while not self.halted and not self.end_of_program:
            self._execute_instruction()

    def _execute_instruction(self):
        # print "0x{:04X}".format(self.state["instruction_pointer"])
        instruction = self._get_next_instruction()

        if instruction != None:
            instruction.execute(self.state)

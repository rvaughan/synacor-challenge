#!/usr/bin/env python
"""
This module attempts to solve the Synacor challenge, this script runs program
zero.

    website: https://challenge.synacor.com/
"""
import logging
import sys

from vm.vm import VM


logging.basicConfig(level=logging.INFO)

vm = VM("challenge.bin")

# Run the first program

# vm.run(start_instruction=0)

with open("instructions.txt", "w") as f:
    vm.run(start_instruction=0, debug=True, debug_file=f)

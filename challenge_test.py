#!/usr/bin/env python
"""
This module attempts to solve the Synacor challenge.

    website: https://challenge.synacor.com/
"""
import logging

from vm.vm import VM


logging.basicConfig(level=logging.INFO)

vm = VM("test.bin")

vm.run(start_instruction=0)

vm.dump_registers()

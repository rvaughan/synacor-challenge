#!/usr/bin/env python
"""
This module attempts to dump the challenge data file.
"""
import logging
import sys

from vm.vm import VM


logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

vm = VM(sys.argv[1])

# Dump the VM
vm.dump(start_instruction=0)

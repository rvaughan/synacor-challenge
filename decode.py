#!/usr/bin/env python
"""
This module attempts to dump the challenge data file.
"""
import logging
import sys

from vm.vm import VM


# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

vm = VM(sys.argv[1])

with open("decoded.txt", "w") as f:
    # Dump the VM
    vm.dump(f, start_instruction=0)

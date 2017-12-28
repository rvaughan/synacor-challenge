#!/usr/bin/env python
"""
This module attempts to solve the Synacor challenge.

    website: https://challenge.synacor.com/
"""
import logging
import sys

from vm.vm import VM


# logging.basicConfig(level=logging.INFO)
logging.basicConfig(level=logging.DEBUG)

vm = VM(sys.argv[1])

# Run the first program
vm.run(start_instruction=0)

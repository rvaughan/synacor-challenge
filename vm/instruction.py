import logging

class Instruction(object):

    def __init__(self):
        pass

    def _get_value(self, vm_state, location):
        if location < 32768:
            return location
        elif location < 32776:
            reg_id = location % 32768
            return vm_state["registers"][reg_id]
        else:
            # Invalid
            logging.info("Invalid value for the JNZ statement. [{0}]".format(location))
            return 0

    def _set_value(self, vm_state, location, value):
        if location < 32768:
            vm_state["memory"][location] = value
        elif location < 32776:
            reg_id = location % 32768
            vm_state["registers"][reg_id] = value
        else:
            # Invalid
            logging.info("Invalid value for the JNZ statement. [{0}]".format(location))

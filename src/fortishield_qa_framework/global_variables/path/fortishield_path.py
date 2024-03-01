"""
Module to build the Fortishield path according to the selected operating system.

This modules contains the following:

- FortishieldPath:
    - get_fortishield_path
"""

import sys
import os

from fortishield_qa_framework.global_variables.platform import WINDOWS, MACOS


class FortishieldPath:
    """Class to build the fortishield paths according to the selected OS.

    Args:
        os_system (str): Operating system.

    Attributes:
        os_system (str): Operating system.
    """
    def __init__(self, os_system=sys.platform):
        self.os_system = os_system

    def get_fortishield_path(self):
        """Get the fortishield path.

        Returns:
            str: Fortishield path.
        """
        if self.os_system == WINDOWS:
            return os.path.join('C:', os.sep, 'Program Files (x86)', 'ossec-agent')
        elif self.os_system == MACOS:
            return os.path.join('/', 'Library', 'Ossec')
        else:
            return os.path.join('/var', 'ossec')

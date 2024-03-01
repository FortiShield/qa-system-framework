"""
Module to build the Fortishield binary paths according to the selected operating system.

This modules contains the following:

- BinaryPath(FortishieldPath):
    - get_binary_path
    - get_agent_control_path
    - get_agent_groups_path
    - get_agent_upgrade_path
    - get_clear_stats_path
    - get_cluster_control_path
    - get_manage_agents_path
    - get_fortishield_control_path
    - get_fortishield_agentlessd_path
    - get_fortishield_analysisd_path
    - get_fortishield_apid_path
    - get_fortishield_authd_path
    - get_fortishield_clusterd_path
    - get_fortishield_csyslogd_path
    - get_fortishield_db_path
    - get_fortishield_dbd_path
    - get_fortishield_execd_path
    - get_fortishield_integratord_path
    - get_fortishield_logcollector_path
    - get_fortishield_logtest_path
    - get_fortishield_maild_path
    - get_fortishield_modulesd_path
    - get_fortishield_monitord_path
    - get_fortishield_regex_path
    - get_fortishield_remoted_path
    - get_fortishield_reportd_path
    - get_fortishield_syscheckd_path
    - get_agent_auth_path
    - get_fortishield_agentd_path
"""

import sys
import os

from fortishield_qa_framework.global_variables.path.fortishield_path import FortishieldPath
from fortishield_qa_framework.global_variables.platform import WINDOWS


class BinaryPath(FortishieldPath):
    """Class to build the fortishield binary paths according to the selected OS.

    Args:
        os_system (str): Operating system.

    Attributes:
        os_system (str): Operating system.
        binary_path (str): Fortishield binary paths.
    """
    def __init__(self, os_system=sys.platform):
        super().__init__(os_system=os_system)
        self.binary_path = os.path.join(self.get_fortishield_path()) if os_system == WINDOWS else \
            os.path.join(self.get_fortishield_path, 'bin')

    def get_binary_path(self):
        return self.binary_path

    def get_agent_control_path(self):
        return os.path.join(self.binary_path, 'agent_control')

    def get_agent_groups_path(self):
        return os.path.join(self.binary_path, 'agent_groups')

    def get_agent_upgrade_path(self):
        return os.path.join(self.binary_path, 'agent_upgrade')

    def get_clear_stats_path(self):
        return os.path.join(self.binary_path, 'clear_stats')

    def get_cluster_control_path(self):
        return os.path.join(self.binary_path, 'cluster_control')

    def get_manage_agents_path(self):
        return os.path.join(self.binary_path, 'manage_agents')

    def get_fortishield_control_path(self):
        return os.path.join(self.binary_path, 'fortishield_control')

    def get_fortishield_agentlessd_path(self):
        return os.path.join(self.binary_path, 'fortishield-agentlessd')

    def get_fortishield_analysisd_path(self):
        return os.path.join(self.binary_path, 'fortishield-analysisd')

    def get_fortishield_apid_path(self):
        return os.path.join(self.binary_path, 'fortishield-apid')

    def get_fortishield_authd_path(self):
        return os.path.join(self.binary_path, 'fortishield-authd')

    def get_fortishield_clusterd_path(self):
        return os.path.join(self.binary_path, 'fortishield-clusterd')

    def get_fortishield_csyslogd_path(self):
        return os.path.join(self.binary_path, 'fortishield-csyslogd')

    def get_fortishield_db_path(self):
        return os.path.join(self.binary_path, 'fortishield-db')

    def get_fortishield_dbd_path(self):
        return os.path.join(self.binary_path, 'fortishield-dbd')

    def get_fortishield_execd_path(self):
        return os.path.join(self.binary_path, 'fortishield-execd')

    def get_fortishield_integratord_path(self):
        return os.path.join(self.binary_path, 'fortishield-integratord')

    def get_fortishield_logcollector_path(self):
        return os.path.join(self.binary_path, 'fortishield-logcollector')

    def get_fortishield_logtest_path(self):
        return os.path.join(self.binary_path, 'fortishield-logtest')

    def get_fortishield_maild_path(self):
        return os.path.join(self.binary_path, 'fortishield-maild')

    def get_fortishield_modulesd_path(self):
        return os.path.join(self.binary_path, 'fortishield-modulesd')

    def get_fortishield_monitord_path(self):
        return os.path.join(self.binary_path, 'fortishield-monitord')

    def get_fortishield_regex_path(self):
        return os.path.join(self.binary_path, 'fortishield-regex')

    def get_fortishield_remoted_path(self):
        return os.path.join(self.binary_path, 'fortishield-remoted')

    def get_fortishield_reportd_path(self):
        return os.path.join(self.binary_path, 'fortishield-reportd')

    def get_fortishield_syscheckd_path(self):
        return os.path.join(self.binary_path, 'fortishield-syscheckd')

    def get_agent_auth_path(self):
        return os.path.join(self.binary_path, 'agent-auth')

    def get_fortishield_agentd_path(self):
        return os.path.join(self.binary_path, 'fortishield-agentd')

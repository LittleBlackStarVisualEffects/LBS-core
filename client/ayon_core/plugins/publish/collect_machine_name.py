"""
Requires:
    none

Provides:
    context     -> machine (str)
"""

import getpass
import socket

import pyblish.api


class CollectMachineName(pyblish.api.ContextPlugin):
    label = "Local Machine Name"
    order = pyblish.api.CollectorOrder - 0.5
    hosts = ["*"]

    def process(self, context):
        machine_name = socket.gethostname()
        username = getpass.getuser()

        machine_value = f"{machine_name}, {username}"
        self.log.info("Machine, user: %s", machine_value)
        context.data["machine"] = machine_value

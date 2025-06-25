import pyblish.api

from ayon_core.lib import get_ayon_username


class CollectCurrentAYONUser(pyblish.api.ContextPlugin):
    """Inject the currently logged on user into the Context"""

    # Order must be after default pyblish-base CollectCurrentUser
    order = pyblish.api.CollectorOrder + 0.001
    label = "Collect AYON User"

    def process(self, context):
        import os
        user = get_ayon_username()
        current_system_user = os.getlogin()
        context.data["user"] = user
        context.data["current_system_user"] = current_system_user
        self.log.debug("Collected user \"{}\"".format(user))
        self.log.debug("before comment \"{}\"".format(context.data["comment"]))
        comment= context.data["comment"]
        user_info = f'{current_system_user} | {context.data["machine"]}'
        new_comment = f'{comment}   |   {user_info}' if comment else user_info
        context.data["comment"] = new_comment
        self.log.debug("after comment \"{}\"".format(context.data["comment"]))



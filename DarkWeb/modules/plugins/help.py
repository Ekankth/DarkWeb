from DarkWeb import *
from DarkWeb.lib import *

from partharjun.help import *

@randydev(command(["help", "helpme"], cmd) & owner)
async def module_help_cmd(client: Client, message: Message):
    await module_help(client, message)

@randydev(command(["plugins"], cmd) & owner)
async def module_helper_cmd(client: Client, message: Message):
    await module_helper(client, message)

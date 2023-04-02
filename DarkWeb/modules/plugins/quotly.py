from DarkWeb import *
from DarkWeb.lib import *

from partharjun.help import add_command_help

@randydev(owner & command(["q"], cmd))
async def quotly_command(bot: Client, message: Message):
    await quotly(bot, message)

add_command_help(
    "quotly", [
        ["q", "Make a quote with reply to message."],
    ]
)

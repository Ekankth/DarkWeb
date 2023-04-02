from DarkWeb import *
from DarkWeb.lib import *

from partharjun.help import *

@randydev(command("restart", cmd) & owner)
async def restart_bot_command(_, message: Message):
    await restart_bot(_, message)

add_command_help(
    "system",
    [
        ["restart", "to restart userbot."],
    ],
)

from DarkWeb import *
from DarkWeb.lib import *

from partharjun.help import add_command_help

@randydev(command(["webshot", "ss"], cmd) & owner)
async def webshot_command(client: Client, message: Message):
    await webshot(client, message)

add_command_help(
    "webshot",
    [
        [f"webshot <link> or .ss <link>", "to screenshot the given web page"],
    ],
)

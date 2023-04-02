from DarkWeb import *
from DarkWeb.lib import *

from partharjun.help import *

@randydev(command(["toonify", "cartoon"], cmd) & owner)
async def toonify_handler(c: Client, m: Message):
    await toonify(c, m)

add_command_help(
    "deepai",
    [
        [f"cartoon or .toonify [reply to image]", "to cartoon image using the deepai api."],
    ],
)

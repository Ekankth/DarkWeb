from DarkWeb import *
from DarkWeb.lib import *

@randydev(command("upload", cmd) & owner)
async def upload_helper_command(bot: Client, message: Message):
    await upload_helper(bot, message)

add_command_help(
    "upload",
    [
        ["upload", "Upload the file to telegram from the given system file path."],
    ],
)

from DarkWeb import *
from DarkWeb.lib import *

@randydev(command("lyrics", cmd) & owner)
async def lyrics_command(client: Client, message: Message):
    await lyrics(client, message)

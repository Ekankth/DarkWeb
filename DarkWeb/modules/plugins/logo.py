from DarkWeb import *
from DarkWeb.lib import *


@randydev(command("logo", cmd) & owner)
async def logo_command(client: Client, message: Message):
    await logo_write(client, message)

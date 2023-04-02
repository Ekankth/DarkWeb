from DarkWeb import *
from DarkWeb.lib import *

from partharjun.help import *

@randydev(command("img", cmd) & owner)
async def generate_image_command(c: Client, m: Message):
    await generate_image(c, m)

from DarkWeb import *
from DarkWeb.lib import *

from partharjun.help import *

@randydev(command("rmbg", cmd) & owner)
async def rmbg_command(c: Client, m: Message):
    await rmbg_background(c, m)

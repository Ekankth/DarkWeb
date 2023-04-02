from DarkWeb import *
from DarkWeb.lib import *

@randydev(command("sysinfo", cmd) & owner)
async def sysinfo_command(c: Client, m: Message):
    await sysinfo(c, m)

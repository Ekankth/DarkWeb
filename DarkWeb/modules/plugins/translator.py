from DarkWeb import *
from DarkWeb.lib import *

from partharjun.help import *

@randydev(command(["tr", "translate"], cmd) & owner)
async def pytrans_tr_command(_, message: Message):
    await pytrans_tr(_, message)

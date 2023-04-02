# Copyright (C) 2020-2023 TeamKillerX <https://github.com/TeamKillerX>
#
# This file is part of TeamKillerX project,
# and licensed under GNU Affero General Public License v3.
# See the GNU Affero General Public License for more details.
#
# All rights reserved. See COPYING, AUTHORS.
#
# Credits by : https://t.me/xtsea
# Don't remove credits

from DarkWeb import *
from DarkWeb.lib import *

from partharjun.help import *

@randydev(command("copy", cmd) & owner)
async def nothing(client: Client, message: Message):
    await copy_message(client, message)

add_command_help(
    "copy",
    [
        [f"copy [link]", "to copy link of public channel"],
    ],
)

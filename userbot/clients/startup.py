# Copyright (C) 2021 The LavanProjects Company LLC.
#
# Licensed under the LavanProjects Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#


# LavanUserBot - Ber4tbey 

import sys

from telethon.utils import get_peer_id

from userbot import BOT_TOKEN
from userbot import LAVAN_VERSION as version
from userbot import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STR2,
    STR3,
    STR4,
    STR5,
    STRING_2,
    STRING_3,
    STRING_4,
    STRING_5,
    STRING_SESSION,
    bot,
    call_py,
    tgbot,
)


EOL = "EOL\nLavanUserbot v{}, Copyright © 2021-2022 LavanderProjects <https://github.com/LavanderProjects>"



async def lavan_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def multilavan():
    if 5159148002 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    
    failed = 0
    if STRING_SESSION:
        try:
            bot.start()
            call_py.start()
            LOOP.run_until_complete(lavan_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION bulundu!\n┌ İsim: {name}\n└ User ID: {uid}\n——"
            )
            
        except Exception as e:
            LOGS.info(str(e))

    if STRING_2:
        try:
            STR2.start()
            LOOP.run_until_complete(lavan_client(STR2))
            user = STR2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_2 bulundu!\n┌ İsim: {name}\n└ User ID: {uid}\n——")
            
        except Exception as e:
            LOGS.info(str(e))

    if STRING_3:
        try:
            STR3.start()
            LOOP.run_until_complete(lavan_client(STR3))
            user = STR3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_3 bulundu!\n┌ İsim: {name}\n└ User ID: {uid}\n——")
            
        except Exception as e:
            LOGS.info(str(e))

    if STRING_4:
        try:
            STR4.start()
            LOOP.run_until_complete(lavan_client(STR4))
            user = STR4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_4 bulundu!\n┌ İsim: {name}\n└ User ID: {uid}\n——")
            
        except Exception as e:
            LOGS.info(str(e))

    if STRING_5:
        try:
            STR5.start()
            LOOP.run_until_complete(lavan_client(STR5))
            user = STR5.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_5 bulundu!\n┌ İsim: {name}\n└ User ID: {uid}\n——")
            
        except Exception as e:
            LOGS.info(str(e))

    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN bulundu!\n┌ İsim: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING_SESSION:
        failed += 1
    if not STRING_2:
        failed += 1
    if not STRING_3:
        failed += 1
    if not STRING_4:
        failed += 1
    if not STRING_5:
        failed += 1
    return failed
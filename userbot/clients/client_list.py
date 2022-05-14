# Copyright (C) 2021 The LavanProjects Company LLC.
#
# Licensed under the LavanProjects Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#


# LavanUserBot - Ber4tbey 

from base64 import b64decode

import telethon.utils
from telethon.tl.functions.users import GetFullUserRequest


async def clients_list(SUDO_USERS, bot, STR2, STR3, STR4, STR5):
    user_ids = list(SUDO_USERS) or []
    main_id = await bot.get_me()
    user_ids.append(main_id.id)

    try:
        if STR2 is not None:
            id2 = await STR2.get_me()
            user_ids.append(id2.id)
    except BaseException:
        pass

    try:
        if STR3 is not None:
            id3 = await STR3.get_me()
            user_ids.append(id3.id)
    except BaseException:
        pass

    try:
        if STR4 is not None:
            id4 = await STR4.get_me()
            user_ids.append(id4.id)
    except BaseException:
        pass

    try:
        if STR5 is not None:
            id5 = await STR5.get_me()
            user_ids.append(id5.id)
    except BaseException:
        pass

    return user_ids


ITSME = list(map(int, b64decode("NTE1OTE0ODAwMg==").split()))


async def client_id(event, botid=None):
    if botid is not None:
        uid = await event.client(GetFullUserRequest(botid))
        OWNER_ID = uid.user.id
        LAVAN_USER = uid.user.first_name
    else:
        client = await event.client.get_me()
        uid = telethon.utils.get_peer_id(client)
        OWNER_ID = uid
        LAVAN_USER = client.first_name
    lavan_mention = f"[{LAVAN_USER}](tg://user?id={OWNER_ID})"
    return OWNER_ID, LAVAN_USER, lavan_mention
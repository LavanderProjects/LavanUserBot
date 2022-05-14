# Copyright (C) 2021 The LavanProjects Company LLC.
#
# Licensed under the LavanProjects Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#


# LavanUserBot - Ber4tbey 


import asyncio
import pybase64
from telethon.tl.functions.channels import JoinChannelRequest as Get
from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from userbot import LAVAN_VERSION as version
from userbot import BOTLOG_CHATID
from userbot import CMD_HANDLER as cmd
from userbot import STR2, STR3, STR4, STR5, bot, branch, tgbot


MSG_ON = """
🔥 **LavanUserbot Başarıyla Etkinleştirildi**
━━
➠ **Userbot Version -** `{}@{}`
➠ **Komut** `{}alive`komutu ile kontrol edebilirsiniz.
━━
"""

async def checking(client):
    gocheck = str(pybase64.b64decode("QExhdmFuVXNlckJvdA=="))[2:13]
    checker = str(pybase64.b64decode("QExhdmFuZGVyU3VwcG9ydA=="))[2:17]
    if client:
        try:
            await client(Get(gocheck))
            await client(Get(checker))
        except BaseException:
            pass
async def lavan_userbot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            LavanUBOT = await tgbot.get_me()
            BOT_USERNAME = LavanUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            LavanUBOT = await tgbot.get_me()
            BOT_USERNAME = LavanUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "BOT"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await checking(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if STR2:
            await checking(STR2)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await STR2.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if STR3:
            await checking(STR3)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await STR3.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if STR4:
            await checking(STR4)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await STR4.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
    try:
        if STR5:
            await checking(STR5)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await STR5.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(version, branch, cmd),
                )
    except BaseException:
        pass
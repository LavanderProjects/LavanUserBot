# Copyright (C) 2022 The LavanderProjects.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# LavanUserBot - Ber4tbey
#
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon import events
import asyncio
from userbot import bot

@register(outgoing=True, disable_errors=True, pattern=r"^\.ftt(?: |$)(.*)")
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, "r")
    c = a.read()
    a.close()
    a = await event.reply("**Dosya Okunuyor...**")
    if len(c) > 4095:
        await a.edit("`Dosya Okunurken Sorun Oluştu.`")
    else:
        await event.client.send_message(event.chat_id, f"```{c}```")
        await a.delete()
    os.remove(b)

    

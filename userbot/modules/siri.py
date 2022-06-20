# Copyright (C) 2022 The LavanderProjects.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# LavanUserBot - Ber4tbey - SakirBey1
#
from telethon import events 
import time 
import asyncio 
from userbot.events import register

@register(outgoing=True,pattern="^.[Ss]iri")

async def komut(event):
        await event.edit("**Alışkanlık İşte**\n __Botumuzun İsmi Değişti Unuttun mu Siri Yazmak Yerine__ `.lavan` __Yazmalısın.__\n \n**Gerekli Açıklama:** t.me/LavanUserBot \n UserBot Kanalı: @LavanUserBot\nPlugin Kanalı: @LavanPlugin")

@register(outgoing=True,pattern="^.[Ee]pic")

async def komut(event):
        await event.edit("**Alışkanlık İşte**\n __Botumuzun İsmi Değişti Unuttun mu Epic Yazmak Yerine__ `.lavan` __Yazmalısın.__\n \n**Gerekli Açıklama:** https://t.me/LavanUserBot \n UserBot Kanalı: @LavanUserBot\nPlugin Kanalı: @LavanPlugin")

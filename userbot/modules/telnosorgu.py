# Copyright (C) 2022 The LavanderProjects.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# LavanUserBot - Ber4tbey
#
# Plugin Sahibi @LavanderProjects & @OfficialAlfa
# Alıcaksan credit bırak

import asyncio
from userbot.events import register
import os
from telethon.tl.functions.channels import JoinChannelRequest
from cmd import Cmd
from telethon import events
from telethon import TelegramClient, events
from multiprocessing.connection import wait
from os import remove
from userbot.cmdhelp import CmdHelp
import datetime
import asyncio
import time
from userbot.events import register



@register(pattern="^.tnosorgu (.*)",outgoing=True)
async def alfasorgu(event):
    number1 = event.pattern_match.group(1)
    try:
        os.system("pip install phonenumbers")
        import phonenumbers
        from phonenumbers import timezone
        from phonenumbers import geocoder
        from phonenumbers import carrier
        await event.edit(f"⚙️{number1} **Nolu telefon numarası sahibinin isteği üzere sorgulanıyor...**")
        time.sleep(1.8)
        number = phonenumbers.parse(number1)
        ax=geocoder.description_for_number(number, 'tr') 
        bx=carrier.name_for_number(number, 'tr') 
        cx=timezone.time_zones_for_number(number)
        dx=phonenumbers.is_valid_number(number)   
        sonuc = f'''

**Sorgu sonuçları kısa bilgiler**

**Telefon numarası dogru mu:** `{dx}`
**Telefon numarası:** `{number1}`
**Ülke:** `{ax}`
**Operatör:** `{bx}`
**Yerel Saat:** `{cx}`
        '''
        await event.edit(sonuc)
    except:
        await event.edit("Hata")
        await event.client(JoinChannelRequest("LavanderUserBot"))
        await event.client(JoinChannelRequest("LavanderSupport"))



Help = CmdHelp('tnosorgu')
Help.add_command('tnosorgu <sorgulamak istediğiniz telefon numarsı(Ülke kodu olarak)>', None, 'Arkadaşınızı korkutmanız için yapılmış basit bir modül🙂',
                 'tnosorgu +90XXXXXXXXXX')
Help.add_info('**@OfficialAlfa tarafından @LavanderProjects için yapılmıştır.**')
Help.add()

# Copyright (C) 2022 The LavanderProjects.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# Lavan UserBot - Ber4tbey
#



from userbot.cmdhelp import CmdHelp
from userbot import cmdhelp
from userbot import CMD_HELP
from userbot.events import register
import aiohttp
import asyncio
import json
import os
from googletrans import LANGUAGES
from emoji import get_emoji_regexp
import random
import html




def deEmojify(inputString):
    """ Emojileri ve diğer güvenli olmayan karakterleri metinden kaldırır. """
    return get_emoji_regexp().sub(u'', inputString)






BOT = "N"

@register(outgoing=True, pattern="^.chatbot ?(.*)")
async def lavan(event):
    global BOT
    if (event.pattern_match.group(1) == "on" or event.pattern_match.group(1) == "aç" or event.pattern_match.group(1) == "ac"):
        if BOT == "Y":
            return await event.edit("**Chatbot Halihazırda Açık!**")

        BOT = "Y"
        await event.edit("**Lavan Yapay Zeka ChatBot Açıldı!**\n**Kullanmak için cümleye** `Lavan` **ile başlayın.**")
    elif (event.pattern_match.group(1) == "off" or event.pattern_match.group(1) == "kapa" or event.pattern_match.group(1) == "kapat"):
        if BOT == "N":
            return await event.edit("**Chatbot Halihazırda Kapalı!**")

        BOT = "N"
        await event.edit("**Lavan Yapay Zeka ChatBot Kapandı!**")
    else:
        await event.edit("**Eksik Parametreler!** \n`.lavan chatbot` **Komutunu kullanarak talimatları okuyun.**")


async def translate_to_msg(text_msg, to):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        async with session.get(f"https://translate.google.com/m?hl=auto&sl=auto&tl={to}&ie=UTF-8&prev=_m&q={text_msg}") as response:

            html = await response.text()
            fin = html.split('result-container">')[1].split('</div>')[0]
            return fin

@register(outgoing=True, disable_edited=False)
async def txt(msg):
    global BOT
    if msg.chat_id == -1001698661722:
        return False
    

    if BOT == "Y":
        message = msg.raw_text
        user_id = msg.sender_id
        if message.startswith("lavan") or message.startswith("Lavan"):
            if message.startswith("lavan"):
                message = message.replace("lavan", "", 1)
            else:
                message = message.replace("Lavan", "", 1)

            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
                aftext = await translate_to_msg(deEmojify(message), "en")
                if aftext == message or aftext == deEmojify(message):
                    return await msg.edit(random.choice((
                        "__Yazdığın cümleyi anlayamıyorum.__",
                        "__Tam olarak ne demek istedin? Anlayamadım.__",
                        "__Sanırım bişey demek istiyorsun fakat anlayamadım.__",
                        "__Daha açıklayıcı konuşurmusun. Pek birşey anlamadım.__",
                        "__Kelimelerini analiz edemiyorum. Cümlene göz atmalısın.__",
                        "__Yazdığın şeyleri anlayamıyorum. Daha düzgün bir şekilde yazar mısın?__",
                        "__Cümlende bir yanlışlık var gibi. Kelimelerini tekrar kontol etmelisin.__",
                        "__Ne? Şeyyy sanırım bunu anlayamadım. Rica etsem daha anlaşılır biçimde yazarmısın?__",
                        "__Üzgünüm ama ne demek istiyorsun? Bence yazdığın şeyi gözden geçir.__",
                        "__Galiba mesajın ile ilgili bir sorun var çünkü ne yazdığını anlayamıyorum..__",
                        "__Heyy heyy bi dakika 🤔 Mesajını kontrol edermisin bunu anlamak gerçekten zor..__",
                        "__Mesajını aldım ama garip bi şekilde anlayamadım :/ Bencee daha açık olman gerekiyor..__",
                        "__Nee?? Sen.. Sen ne yazdın? Dostum yazdığın şeyi anlamam gerçekten çok zor..__",
                        "__Bip Bop! 👽 Tanrısal güçlerim yazdığın mesajın garip olduğunu söylüyor. Mesajını kontrol et insan!__",
                        "__Evet haklısın insan eti çok ta.. Ah mesajını aldım. Ama bi sorun var. Anlayamıyorum? Mesajını düzeltebilir misin? Bu arada birşey duymadın demi?__",
                        "__Hızlandırılmış Türkçe Dersi > Yükle! Niye? Çünkü sanal beynim mesajını anlamadı..__",
                        "__Şöyle yapalım. Sen mesajını daha anlaşılır bir şekilde yeniden yaz, daha yaz sonra beni tekrar çağır 😊__",
                        "__Cümle Analizi Başlıyor.. Analiz Bitti.. Cümle Anlaşılamadı! İstek Gönder: Lütfen daha anlaşılır biçimde yazın.__",
                        "__Seni severim, bilirsin ama cümlelerini daha anlaşılır yazarsan daha iyi anlaşabiliriz.__",
                        "__Rose!! Rose, baksana yine anlayamadığım mesajlar yazıyor.. Ona daha anlaşılır yazmasını söylesene. Heyy, biraz daha açık olur musun :)__",
                        "__3 dilek hakkım olsa 3'ünü de senin daha anlaşılır mesaj yazmanı dilemek için harcardım..__",
                        "__Yılın sorusu geliyor.. Az önce ne yazdın?? Ben bir makinayım biraz daha açık olmalısın.__"))
                    )
                    
                async with session.get('https://open-apis-rest.up.railway.app/api/chatbot?id=' + str(user_id) + f"&message={aftext}") as response: # THX Phaticusthiccy For APİ
                
                    html = await response.text()
                    html2 = json.loads(html)
                    if html2["status"] == "OK":
                        try:
                            fin_msg = html.unescape(html2["data"])
                        except:
                            fin_msg = html2["data"]
                            
                        outtext = await translate_to_msg(fin_msg, "tr")
                        await msg.client.send_message(msg.chat_id, f"{outtext}", reply_to=msg, link_preview=False)
                    else:
                        if "Message" in html2["error"]:
                            return await msg.edit("__Seni anlamam için birşeyler yazmalısın..__")

        else:
            return False
    else:
	    return False



Help = CmdHelp('chatbot')
Help.add_command('chatbot', 
    '<on / off veya ac / kapa>', 
    'Yapay Zeka Sohbet Botunu Aktif Eder.',
    'chatbot on \nchatbot off'
)
Help.add_info("Thx @phaticusthiccy")
Help.add()

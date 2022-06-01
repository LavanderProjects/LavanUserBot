import asyncio
import importlib
import logging
import sys
from pathlib import Path
from random import randint

import heroku3
from telethon.tl.functions.channels import CreateChannelRequest
from telethon.tl.functions.contacts import UnblockRequest

from userbot import (
    BOT_TOKEN,
    BOTLOG_CHATID,
    CMD_HELP,
    HEROKU_APIKEY,
    HEROKU_APPNAME,
    LOGS,
    bot,
)

heroku_api = "https://api.heroku.com"
if HEROKU_APPNAME is not None and HEROKU_APIKEY is not None:
    Heroku = heroku3.from_key(HEROKU_APIKEY)
    app = Heroku.app(HEROKU_APPNAME)
    heroku_var = app.config()
else:
    app = None


async def autopilot():
    LOGS.info("BİRAZ BEKLE. SİZİN İÇİN USERBOT LOGG RUBU OLUŞTURULUYOR")
    desc = "LavanUserbot için Log grubu.\n\nLÜTFEN BU GRUPTAN AYRILMAYIN.\n\n✨ Powered by ~ @LavanderProjects ✨"
    try:
        grup = await bot(
            CreateChannelRequest(title="LavanUB Log", about=desc, megagroup=True)
        )
        grup_id = grup.chats[0].id
    except Exception as e:
        LOGS.error(str(e))
        LOGS.warning(
            "BOTLOG_CHATID değişkeniniz girilmedi. Bir telegram grubu oluşturun ve bot @MissRose_bot girin, ardından /id yazın Grup kimliğini var BOTLOG_CHATID içine girin"
        )
    if not str(grup_id).startswith("-100"):
        grup_id = int(f"-100{str(grup_id)}")
    heroku_var["BOTLOG_CHATID"] = grup_id


async def autobot():
    if BOT_TOKEN:
        return
    await bot.start()
    await asyncio.sleep(15)
    await bot.send_message(
        BOTLOG_CHATID, "**@BotFather'DA SİZİN İÇİN BİR TELEGRAM BOTU OLUŞTURULUYOR**"
    )
    LOGS.info("BİRAZ BEKLE. SİZİN İÇİN YARDIMCI BOTLAR YAPIYORUZ")
    who = await bot.get_me()
    name = f"{who.first_name} Assistant Bot"
    if who.username:
        username = f"{who.username}_ubot"
    else:
        username = f"Lavan{(str(who.id))[5:]}ubot"
    bf = "@BotFather"
    await bot(UnblockRequest(bf))
    await bot.send_message(bf, "/cancel")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/start")
    await asyncio.sleep(1)
    await bot.send_message(bf, "/newbot")
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if isdone.startswith("That I cannot do."):
        LOGS.info(
            "Lütfen @BotFather'dan bir Bot oluşturun ve tokeni  BOT_TOKEN içine ekleyin"
        )
        sys.exit(1)
    await bot.send_message(bf, name)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    if not isdone.startswith("Good."):
        await bot.send_message(bf, "My Assistant Bot")
        await asyncio.sleep(1)
        isdone = (await bot.get_messages(bf, limit=1))[0].text
        if not isdone.startswith("Good."):
            LOGS.info(
                "Lütfen @BotFather'dan bir Bot oluşturun ve tokeni  BOT_TOKEN içine ekleyin"
            )
            sys.exit(1)
    await bot.send_message(bf, username)
    await asyncio.sleep(1)
    isdone = (await bot.get_messages(bf, limit=1))[0].text
    await bot.send_read_acknowledge("botfather")
    if isdone.startswith("Sorry,"):
        ran = randint(1, 100)
        username = f"man{(str(who.id))[6:]}{str(ran)}ubot"
        await bot.send_message(bf, username)
        await asyncio.sleep(1)
        nowdone = (await bot.get_messages(bf, limit=1))[0].text
        if nowdone.startswith("Done!"):
            token = nowdone.split("`")[1]
            await bot.send_message(bf, "/setinline")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(bf, "Search")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_file(bf, "image/lavan.jpg")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setabouttext")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"Managed With ☕️ By {who.first_name}")
            await asyncio.sleep(3)
            await bot.send_message(bf, "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message(bf, f"@{username}")
            await asyncio.sleep(1)
            await bot.send_message(
                bf, f"✨ Owner ~ {who.first_name} ✨\n\n✨ Powered By ~ @LavanderProjects ✨"
            )
            await bot.send_message(
                BOTLOG_CHATID,
                f"**KULLANICI ADI İLE BAŞARIYLA BİR TELEGRAM BOTU OLUŞTURULUYOR @{username}**",
            )
            LOGS.info(f"KULLANICI ADI İLE BAŞARIYLA BİR TELEGRAM BOTU OLUŞTURULUYOR @{username}")
            await bot.send_message(
                BOTLOG_CHATID,
                "**Bir dakika bekleyin, Değişiklikleri Uygulamak için Heroku'yu Yeniden Başlatın.**",
            )
            heroku_var["BOT_TOKEN"] = token
        else:
            LOGS.info(
                "Lütfen @Botfather'daki Telegram Botlarınızdan Bazılarını Silin veya  BOT_TOKEN'ı bot TOKENİNİ ayarlayın"
            )
            sys.exit(1)
    elif isdone.startswith("Done!"):
        token = isdone.split("`")[1]
        await bot.send_message(bf, "/setinline")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(bf, "Search")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setuserpic")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_file(bf, "image/lavan.jpg")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setabouttext")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"Managed With ☕️ By {who.first_name}")
        await asyncio.sleep(3)
        await bot.send_message(bf, "/setdescription")
        await asyncio.sleep(1)
        await bot.send_message(bf, f"@{username}")
        await asyncio.sleep(1)
        await bot.send_message(
            bf, f"✨ Owner ~ {who.first_name} ✨\n\n✨ Powered By ~ @LavanderProjects ✨"
        )
        await bot.send_message(
            BOTLOG_CHATID,
            f"**KULLANICI ADI İLE BAŞARIYLA BİR TELEGRAM BOTU OLUŞTURULUYOR @{username}**",
        )
        LOGS.info(f"KULLANICI ADI İLE BAŞARIYLA BİR TELEGRAM BOTU OLUŞTURULUYOR @{username}")
        await bot.send_message(
            BOTLOG_CHATID,
            "**Bir dakika bekleyin, Değişiklikleri Uygulamak için Heroku'yu Yeniden Başlatın.**",
        )
        heroku_var["BOT_TOKEN"] = token
    else:
        LOGS.info(
            "Lütfen @Botfather'daki Telegram Botlarınızdan Bazılarını Silin veya  BOT_TOKEN'ı bot TOKENİNİ ayarlayın"
        )
        sys.exit(1)


def load_module(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"userbot/modules/{shortname}.py")
        name = f"userbot.modules.{shortname}"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info(f"Successfully imported {shortname}")
    else:

        path = Path(f"userbot/modules/{shortname}.py")
        name = f"userbot.modules.{shortname}"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = bot
        mod.LOGS = LOGS
        mod.CMD_HELP = CMD_HELP
        mod.logger = logging.getLogger(shortname)
        spec.loader.exec_module(mod)
        # for imports
        sys.modules[f"userbot.modules.{shortname}"] = mod
        LOGS.info(f"Successfully imported {shortname}")


def start_assistant(shortname):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"userbot/assistant/{shortname}.py")
        name = f"userbot.assistant.{shortname}"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info("Starting Your Assistant Bot.")
        LOGS.info(f"Assistant Sucessfully imported {shortname}")
    else:
        path = Path(f"userbot/assistant/{shortname}.py")
        name = f"userbot.assistant.{shortname}"
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.tgbot = bot.tgbot
        spec.loader.exec_module(mod)
        sys.modules[f"userbot.assistant{shortname}"] = mod
        LOGS.info(f"Assistant Successfully imported{shortname}")


def remove_plugin(shortname):
    try:
        try:
            for i in CMD_HELP[shortname]:
                bot.remove_event_handler(i)
            del CMD_HELP[shortname]

        except BaseException:
            name = f"userbot.modules.{shortname}"

            for i in reversed(range(len(bot._event_builders))):
                cb = bot._event_builders[i]
                if cb.__module__ == name:
                    del bot._event_builders[i]
    except BaseException:
        raise ValueError

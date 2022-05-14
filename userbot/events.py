# Copyright (C) 2022 The  LavanderProjects.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# LavanUserBot - Ber4tbey

""" Olayları yönetmek için UserBot modülü.
 UserBot'un ana bileşenlerinden biri. """
import re
from requests import get
import sys
from asyncio import create_subprocess_shell as asyncsubshell
from asyncio import subprocess as asyncsub
from os import remove
from time import gmtime, strftime
from traceback import format_exc
from telethon import events
import base64
from userbot import bot, BOTLOG_CHATID, LOGSPAMMER, PATTERNS, LAVAN_VERSION, ForceVer
from telethon.tl.functions.channels import JoinChannelRequest
from userbot import PATTERNS, DEVS, STR2, STR3, STR4, STR5, bot
import inspect
from pathlib import Path


CMD_LIST = {}

def lavan_cmd(pattern=None, comSTR5=None, **args):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")
    args.get("allow_sudo", False)
    if pattern is not None:
        if pattern.startswith(r"\#"):
            args["pattern"] = re.compile(pattern)
        elif pattern.startswith(r"^"):
            args["pattern"] = re.compile(pattern)
            cmd = pattern.replace("$", "").replace("^", "").replace("\\", "")
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
        else:
            if len(PATTERNS) == 2:
                catreg = "^" + PATTERNS
                reg = PATTERNS[1]
            elif len(PATTERNS) == 1:
                catreg = "^\\" + PATTERNS
                reg = PATTERNS
            args["pattern"] = re.compile(catreg + pattern)
            if comSTR5 is not None:
                cmd = reg + comSTR5
            else:
                cmd = (
                    (reg + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})

    if "allow_edited_updates" in args and args["allow_edited_updates"]:
        del args["allow_edited_updates"]

    return events.NewMessage(**args)


def comSTR5(**args):
    args["func"] = lambda e: e.via_bot_id is None

    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    pattern = args.get("pattern")
    allow_edited_updates = args.get("allow_edited_updates", False)
    args["incoming"] = args.get("incoming", False)
    args["outgoing"] = True
    if bool(args["incoming"]):
        args["outgoing"] = False

    try:
        if pattern is not None and not pattern.startswith("(?i)"):
            args["pattern"] = "(?i)" + pattern
    except BaseException:
        pass

    reg = re.compile("(.*)")
    if pattern is not None:
        try:
            cmd = re.search(reg, pattern)
            try:
                cmd = cmd.group(1).replace("$", "").replace("\\", "").replace("^", "")
            except BaseException:
                pass
            try:
                CMD_LIST[file_test].append(cmd)
            except BaseException:
                CMD_LIST.update({file_test: [cmd]})
        except BaseException:
            pass


def register(**args):
    """ Yeni bir etkinlik kaydedin. """
    pattern = args.get('pattern', None)
    disable_edited = args.get('disable_edited', False)
    groups_only = args.get('groups_only', False)
    trigger_on_fwd = args.get('trigger_on_fwd', False)
    trigger_on_inline = args.get('trigger_on_inline', False)
    disable_errors = args.get('disable_errors', False)

    if pattern:
        args["pattern"] = pattern.replace("^.", "^["+ PATTERNS + "]")
    if "disable_edited" in args:
        del args['disable_edited']

    if "ignore_unsafe" in args:
        del args['ignore_unsafe']

    if "groups_only" in args:
        del args['groups_only']

    if "disable_errors" in args:
        del args['disable_errors']

    if "trigger_on_fwd" in args:
        del args['trigger_on_fwd']
      
    if "trigger_on_inline" in args:
        del args['trigger_on_inline']

    def decorator(func):
        async def wrapper(check):
         
          
          
            LAVANVer = int(LAVAN_VERSION.split(".")[1])
            if ForceVer > LAVANVer:
                await check.edit(f"`🌈 Botu acilen güncellemen lazım! Bu sürüm artık kullanılamıyor..`\n\n__🥺 Sorunu çözmek için__ `.update now` __yazmalısın!__")
                return

            if not LOGSPAMMER:
                send_to = check.chat_id
            else:
                send_to = BOTLOG_CHATID

            if not trigger_on_fwd and check.fwd_from:
                return

            if check.via_bot_id and not trigger_on_inline:
                return
             
            if groups_only and not check.is_group:
                await check.respond("`⛔ Bunun bir grup olduğunu sanmıyorum. Bu plugini bir grupta dene! `")
                return

            try:
                await func(check)
                

            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except AttributeError:
                pass
            except BaseException:
                if not disable_errors:
                    date = strftime("%Y-%m-%d %H:%M:%S", gmtime())

                    eventtext = str(check.text)
                    text = "**🛑USERBOT HATA RAPORU🛑**\n"
                    link = "[Lavan Destek Grubuna](https://t.me/LavanderSupport)"
                    if len(eventtext)<10:
                        text += f"\n**🗒️ Şu yüzden:** {eventtext}\n"
                    text += "\nℹ️ İsterseniz, bunu bildirebilirsiniz."
                    text += f"- sadece bu mesajı {link} gönderin.\n"
                    text += "Hata ve tarih haricinde hiçbir şey kayıt edilmez.\n"

                    ftext = "========== UYARI =========="
                    ftext += "\nBu dosya sadece burada yüklendi,"
                    ftext += "\nSadece hata ve tarih kısmını kaydettik,"
                    ftext += "\nGizliliğinize saygı duyuyoruz,"
                    ftext += "\nBurada herhangi bir gizli veri varsa"
                    ftext += "\nBu hata raporu olmayabilir, kimse verilerinize ulaşamaz.\n"
                    ftext += "--------USERBOT HATA GUNLUGU--------\n"
                    ftext += "\nTarih: " + date
                    ftext += "\nGrup ID: " + str(check.chat_id)
                    ftext += "\nGönderen kişinin ID: " + str(check.sender_id)
                    ftext += "\n\nOlay Tetikleyici:\n"
                    ftext += str(check.text)
                    ftext += "\n\nHata metni:\n"
                    ftext += str(sys.exc_info()[1])
                    ftext += "\n\n\nGeri izleme bilgisi:\n"
                    ftext += str(format_exc())
                    ftext += "\n\n--------USERBOT HATA GUNLUGU BITIS--------"
                    ftext += "\n\n================================\n"
                    ftext += f"====== BOTVER : {LAVAN_VERSION} ======\n"
                    ftext += "======  Powered by LavanderProjects   ======"
                    ftext += "================================"

                    comSTR5 = "git log --pretty=format:\"%an: %s\" -7"

                    ftext += "\n\n\nSon 7 commit:\n"

                    process = await asyncsubshell(comSTR5,
                                                  stdout=asyncsub.PIPE,
                                                  stderr=asyncsub.PIPE)
                    stdout, stderr = await process.communicate()
                    result = str(stdout.decode().strip()) \
                        + str(stderr.decode().strip())

                    ftext += result

                    file = open("error.log", "w+")
                    file.write(ftext)
                    file.close()

                    if LOGSPAMMER:
                        try:
                            await check.edit("`❕ Üzgünüm, UserBot bir hatayla karşılaştı.\n ℹ️ Hata günlükleri UserBot günlük grubunda saklanır.`")
                        except:
                            pass
                    await check.client.send_file(send_to,
                                                 "error.log",
                                                 caption=text)

                    remove("error.log")
            else:
                pass
        if bot:
            if not disable_edited:
                bot.add_event_handler(wrapper, events.MessageEdited(**args))
            bot.add_event_handler(wrapper, events.NewMessage(**args))
        if STR2:
            if not disable_edited:
                STR2.add_event_handler(wrapper, events.MessageEdited(**args))
            STR2.add_event_handler(wrapper, events.NewMessage(**args))
        if STR3:
            if not disable_edited:
                STR3.add_event_handler(wrapper, events.MessageEdited(**args))
            STR3.add_event_handler(wrapper, events.NewMessage(**args))
        if STR4:
            if not disable_edited:
                STR4.add_event_handler(wrapper, events.MessageEdited(**args))
            STR4.add_event_handler(wrapper, events.NewMessage(**args))
        if STR5:
            if not disable_edited:
                STR5.add_event_handler(wrapper, events.MessageEdited(**args))
            STR5.add_event_handler(wrapper, events.NewMessage(**args))
        return wrapper

    return decorator
                
            

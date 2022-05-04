# Copyright (C) 2022 The LavanderProjects.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# LavanUserBot - Ber4tbey
#

from userbot.events import register
from userbot import CMD_HELP, bot, LOGS, CLEAN_WELCOME, BOTLOG_CHATID
from telethon.events import ChatAction
from userbot.cmdhelp import CmdHelp


# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("welcome")

# ████████████████████████████████ #
try:
    from userbot.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError

from sqlalchemy import BigInteger, Column, Numeric, String, UnicodeText


class Welcome(BASE):
    __tablename__ = "welcome"
    chat_id = Column(String(14), primary_key=True)
    previous_welcome = Column(BigInteger)
    reply = Column(UnicodeText)
    f_mesg_id = Column(Numeric)

    def __init__(self, chat_id, previous_welcome, reply, f_mesg_id):
        self.chat_id = str(chat_id)
        self.previous_welcome = previous_welcome
        self.reply = reply
        self.f_mesg_id = f_mesg_id


Welcome.__table__.create(checkfirst=True)


def get_welcome(chat_id):
    try:
        return SESSION.query(Welcome).get(str(chat_id))
    finally:
        SESSION.close()


def get_current_welcome_settings(chat_id):
    try:
        return SESSION.query(Welcome).filter(
            Welcome.chat_id == str(chat_id)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def add_welcome_setting(chat_id, previous_welcome, reply, f_mesg_id):
    to_check = get_welcome(chat_id)
    if not to_check:
        adder = Welcome(chat_id, previous_welcome, reply, f_mesg_id)
        SESSION.add(adder)
        SESSION.commit()
        return True
    else:
        rem = SESSION.query(Welcome).get(str(chat_id))
        SESSION.delete(rem)
        SESSION.commit()
        adder = Welcome(chat_id, previous_welcome, reply, f_mesg_id)
        SESSION.commit()
        return False


def rm_welcome_setting(chat_id):
    try:
        rem = SESSION.query(Welcome).get(str(chat_id))
        if rem:
            SESSION.delete(rem)
            SESSION.commit()
            return True
    except BaseException:
        return False


def update_previous_welcome(chat_id, previous_welcome):
    row = SESSION.query(Welcome).get(str(chat_id))
    row.previous_welcome = previous_welcome
    SESSION.commit()

@bot.on(ChatAction)
async def welcome_to_chat(event):
    
    cws = get_current_welcome_settings(event.chat_id)
    if cws:
        """user_added=True,
        user_joined=True,
        user_left=False,
        user_kicked=False"""
        if (event.user_joined
                or event.user_added) and not (await event.get_user()).bot:
            if CLEAN_WELCOME:
                try:
                    await event.client.delete_messages(event.chat_id,
                                                       cws.previous_welcome)
                except Exception as e:
                    LOGS.warn(str(e))
            a_user = await event.get_user()
            chat = await event.get_chat()
            me = await event.client.get_me()

            title = chat.title if chat.title else "this chat"
            participants = await event.client.get_participants(chat)
            count = len(participants)
            mention = "[{}](tg://user?id={})".format(a_user.first_name,
                                                     a_user.id)
            my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
            first = a_user.first_name
            last = a_user.last_name
            if last:
                fullname = f"{first} {last}"
            else:
                fullname = first
            username = f"@{a_user.username}" if a_user.username else mention
            userid = a_user.id
            my_first = me.first_name
            my_last = me.last_name
            if my_last:
                my_fullname = f"{my_first} {my_last}"
            else:
                my_fullname = my_first
            my_username = f"@{me.username}" if me.username else my_mention
            file_media = None
            current_saved_welcome_message = None
            if cws and cws.f_mesg_id:
                msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                        ids=int(cws.f_mesg_id))
                file_media = msg_o.media
                current_saved_welcome_message = msg_o.message
            elif cws and cws.reply:
                current_saved_welcome_message = cws.reply
            current_message = await event.reply(
                current_saved_welcome_message.format(mention=mention,
                                                     title=title,
                                                     count=count,
                                                     first=first,
                                                     last=last,
                                                     fullname=fullname,
                                                     username=username,
                                                     userid=userid,
                                                     my_first=my_first,
                                                     my_last=my_last,
                                                     my_fullname=my_fullname,
                                                     my_username=my_username,
                                                     my_mention=my_mention),
                file=file_media)
            update_previous_welcome(event.chat_id, current_message.id)


@register(outgoing=True, pattern=r"^.setwelcome(?: |$)(.*)")
async def save_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import add_welcome_setting
    except:
        await event.edit("`SQL dışı modda çalışıyor!`")
        return
    msg = await event.get_reply_message()
    string = event.pattern_match.group(1)
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await event.client.send_message(
                BOTLOG_CHATID, f"#KARSILAMA_NOTU\
            \nGRUP ID: {event.chat_id}\
            \nAşağıdaki mesaj sohbet için yeni Karşılama notu olarak kaydedildi, lütfen silmeyin !!"
            )
            msg_o = await event.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=event.chat_id,
                silent=True)
            msg_id = msg_o.id
        else:
            await event.edit(
                "`Karşılama notunu kaydetmek için BOTLOG_CHATID ayarlanması gerekir.`"
            )
            return
    elif event.reply_to_msg_id and not string:
        rep_msg = await event.get_reply_message()
        string = rep_msg.text
    success = "`Karşılama mesajı bu sohbet için {} `"
    if add_welcome_setting(event.chat_id, 0, string, msg_id) is True:
        await event.edit(success.format('kaydedildi'))
    else:
        await event.edit(success.format('güncellendi'))


@register(outgoing=True, pattern="^.checkwelcome$")
async def show_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import get_current_welcome_settings
    except:
        await event.edit("`SQL dışı modda çalışıyor!`")
        return
    cws = get_current_welcome_settings(event.chat_id)
    if not cws:
        await event.edit("`Burada kayıtlı karşılama mesajı yok.`")
        return
    elif cws and cws.f_mesg_id:
        msg_o = await event.client.get_messages(entity=BOTLOG_CHATID,
                                                ids=int(cws.f_mesg_id))
        await event.edit(
            "`Şu anda bu karşılama notu ile yeni kullanıcıları ağırlıyorum.`")
        await event.reply(msg_o.message, file=msg_o.media)
    elif cws and cws.reply:
        await event.edit(
            "`Şu anda bu karşılama notu ile yeni kullanıcıları ağırlıyorum.`")
        await event.reply(cws.reply)


@register(outgoing=True, pattern="^.rmwelcome$")
async def del_welcome(event):
    try:
        from userbot.modules.sql_helper.welcome_sql import rm_welcome_setting
    except:
        await event.edit("`SQL dışı modda çalışıyor!`")
        return
    if rm_welcome_setting(event.chat_id) is True:
        await event.edit("`Karşılama mesajı bu sohbet için silindi.`")
    else:
        await event.edit("`Burada karşılama notu var mı ?`")

CmdHelp('welcome').add_command(
    'setwelcome', LANG['WEL1'], LANG['WEL2']
).add_command(
    'checkwelcome', None, LANG['WEL3']
).add_command(
    'rmwelcome', None, LANG['WEL4']
).add_info(LANG['WEL5']).add()

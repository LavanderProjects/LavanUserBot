import asyncio
import inspect
import re
from pathlib import Path

from telethon import events
from telethon.errors import (
    AlreadyInConversationError,
    BotInlineDisabledError,
    BotResponseTimeoutError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
    ChatSendStickersForbiddenError,
    FloodWaitError,
    MessageIdInvalidError,
    MessageNotModifiedError,
)
from userbot import PATTERNS
from userbot import (
    CMD_LIST,
    LOGS,
    PATTERNS,
    STR2,
    STR3,
    STR4,
    STR5,
    SUDO_HANDLER,
    SUDO_USERS,
    bot,
    tgbot,
)

from .tools import edit_delete


def lavan_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    group_only: bool = False,
    admins_only: bool = False,
    private_only: bool = False,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    
    if pattern is not None:
        global man_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            man_reg = sudo_reg = re.compile(pattern)
        else:
            man_ = "\\" + PATTERNS
            sudo_ = "\\" + SUDO_HANDLER
            man_reg = re.compile(man_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = man_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (man_ + pattern).replace("$", "").replace("\\", "").replace("^", "")
                )
                cmd2 = (
                    (sudo_ + pattern)
                    .replace("$", "")
                    .replace("\\", "")
                    .replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})

    def decorator(func):
        async def wrapper(event):
            chat = event.chat
            if admins_only:
                if event.is_private:
                    return await edit_delete(
                        event, "**Bu komut sadece gruplarda kullanılabilir.**", 10
                    )
                if not (chat.admin_rights or chat.creator):
                    return await edit_delete(
                        event, f"**{chat.title} grubunda yönetici olmadığın için üzgünüm**", 10
                    )
            if group_only and not event.is_group:
                return await edit_delete(
                    event, "**Bu komut sadece gruplarda kullanılabilir.**", 10
                )
            if private_only and not event.is_private:
                return await edit_delete(
                    event, "**Bu komut sadece özel sohbette kullanılabilir.**", 10
                )
            try:
                await func(event)
            
            except MessageNotModifiedError as er:
                LOGS.error(er)
            except MessageIdInvalidError as er:
                LOGS.error(er)
            except BotInlineDisabledError:
                await edit_delete(
                    event, "**Lütfen botlar için Satır içi modu etkinleştirin**", 10
                )
            except ChatSendStickersForbiddenError:
                await edit_delete(
                    event, "**Bu sohbette çıkartma gönderilemiyor**", 10
                )
            except BotResponseTimeoutError:
                await edit_delete(
                    event, "**Bot, sorgunuza zamanında cevap vermedi**"
                )
            except ChatSendMediaForbiddenError:
                await edit_delete(
                    event, "**Bu sohbette medya gönderilemiyor**", 10
                )
            except AlreadyInConversationError:
                await edit_delete(
                    event,
                    "**Görüşme, verilen sohbetle zaten gerçekleşiyor. bir süre sonra tekrar deneyin.**",
                )
            except ChatSendInlineForbiddenError:
                await edit_delete(
                    event,
                    "**Bu sohbette satır içi mesajlar gönderilemiyor.**",
                    10,
                )
            except FloodWaitError as e:
                LOGS.error(
                    f"Bir FloodWait hatası oluştu, {e.seconds} saniye bekleyin ve tekrar deneyin"
                )
                await event.delete()
                await asyncio.sleep(e.seconds + 5)
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException as e:
                LOGS.exception(e)

        if bot:
            if not disable_edited:
                bot.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=man_reg),
                )
            bot.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=man_reg)
            )
        if bot:
            if allow_sudo:
                if not disable_edited:
                    bot.add_event_handler(
                        wrapper,
                        events.MessageEdited(
                            **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                        ),
                    )
                bot.add_event_handler(
                    wrapper,
                    events.NewMessage(
                        **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                    ),
                )
        if STR2:
            if not disable_edited:
                STR2.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=man_reg),
                )
            STR2.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=man_reg)
            )
        if STR3:
            if not disable_edited:
                STR3.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=man_reg),
                )
            STR3.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=man_reg)
            )
        if STR4:
            if not disable_edited:
                STR4.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=man_reg),
                )
            STR4.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=man_reg)
            )
        if STR5:
            if not disable_edited:
                STR5.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=man_reg),
                )
            STR5.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=man_reg)
            )
    

    return decorator


def lavan_handler(
    **args,
):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.NewMessage(**args))
        if STR2:
            STR2.add_event_handler(func, events.NewMessage(**args))
        if STR3:
            STR3.add_event_handler(func, events.NewMessage(**args))
        if STR4:
            STR4.add_event_handler(func, events.NewMessage(**args))
        if STR5:
            STR5.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator





def chataction(**args):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.ChatAction(**args))
        if STR2:
            STR2.add_event_handler(func, events.ChatAction(**args))
        if STR3:
            STR3.add_event_handler(func, events.ChatAction(**args))
        if STR4:
            STR4.add_event_handler(func, events.ChatAction(**args))
        if STR5:
            STR5.add_event_handler(func, events.ChatAction(**args))
        return func

    return decorator


def callback(**args):
    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator

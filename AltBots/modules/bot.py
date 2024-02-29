import sys
import heroku3

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10, OWNER_ID, SUDO_USERS, HEROKU_APP_NAME, HEROKU_API_KEY, CMD_HNDLR as hl

from os import execl, getenv
from telethon import events
from datetime import datetime


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
        start = datetime.now()
        altron = await e.reply(f"»⚡ᴛᴇᴀᴍ 𝐅ʟ𝟒ᴍᴇ ᴏɴ ᴛᴏᴘ⚡")
        end = datetime.now()
        mp = (end - start).microseconds / 1000
        await altron.edit(f"🔥𝐅ʟ𝟒ᴍᴇ𝑋sᴘᴀᴍ 𝗕𝗢𝗧𝗦 𝗗𝗨𝗦𝗛𝗠𝗔𝗡𝗢 𝗞𝗜 𝗠𝗔𝗔 𝗖𝗛𝗢𝗗𝗡𝗘 𝗞𝗢 𝗧𝗔𝗜𝗬𝗔𝗥 𝗛𝗔𝗜🔥\n» {mp} 𝙼𝚂")


@X1.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sreboot(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        await e.reply(f"⚡𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝐅ʟ𝟒ᴍᴇ𝑋sᴘᴀᴍ 𝙱𝙾𝚃𝚂⚡ᴘʟs ᴡᴀɪᴛ...")
        try:
            await X1.disconnect()
        except Exception:
            pass
        try:
            await X2.disconnect()
        except Exception:
            pass
        try:
            await X3.disconnect()
        except Exception:
            pass
        try:
            await X4.disconnect()
        except Exception:
            pass
        try:
            await X5.disconnect()
        except Exception:
            pass
        try:
            await X6.disconnect()
        except Exception:
            pass
        try:
            await X7.disconnect()
        except Exception:
            pass
        try:
            await X8.disconnect()
        except Exception:
            pass
        try:
            await X9.disconnect()
        except Exception:
            pass
        try:
            await X10.disconnect()
        except Exception:
            pass

        execl(sys.executable, sys.executable, *sys.argv)


@X1.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%ssudo(?: |$)(.*)" % hl))
async def addsudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"» 𝙰𝙳𝙳𝙸𝙽𝙶 𝚄𝚂𝙴𝚁 𝙰𝚂 🔥𝐅ʟ𝟒ᴍᴇ𝑋sᴘᴀᴍ🔥 𝚂𝚄𝙳𝙾...⚡⚡")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("[HEROKU]:" "\nPlease Setup Your HEROKU_APP_NAME")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁 ʙᴏss 🙄 !!")
            return

        if str(target) in sudousers:
            await ok.edit("» 𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝙸𝚂 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙰 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁 𝙾𝙵 𝐅ʟ𝟒ᴍᴇ𝑋sᴘᴀᴍ 𝙱𝙾𝚃𝚂 ʙᴏss🙄!!")
        else:
            if len(sudousers) > 0:
                newsudo = f"{sudousers} {target}"
            else:
                newsudo = f"{target}"
            await ok.edit(f"» 𝙽𝙴𝚆 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁: {target}\n» ⚡𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 𝐅ʟ𝟒ᴍᴇ𝑋sᴘᴀᴍ 𝙱𝙾𝚃𝚂⚡ᴘʟs ᴡᴀɪᴛ...`")
            heroku_var["SUDO_USERS"] = newsudo    
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» 𝚂𝙾𝚁𝚁𝚈, 𝙾𝙽𝙻𝚈 𝙾𝚆𝙽𝙴𝚁 𝙲𝙰𝙽 𝙰𝙲𝙴𝚂𝚂 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳 𝙱𝙾𝚂𝚂😅.")

        
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sremovesudo(?: |$)(.*)" % hl))
async def removesudo(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        ok = await event.reply(f"» 𝚁𝙴𝙼𝙾𝚅𝙸𝙽𝙶 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁 𝙰𝚂 𝐅ʟ𝟒ᴍᴇ𝑋sᴘᴀᴍ 𝚂𝚄𝙳𝙾...⚡⚡")
        target = ""
        if HEROKU_APP_NAME is not None:
            app = Heroku.app(HEROKU_APP_NAME)
        else:
            await ok.edit("[HEROKU]:" "\nPlease Setup Your HEROKU_APP_NAME")
            return
        heroku_var = app.config()
        if event is None:
            return
        try:
            reply_msg = await event.get_reply_message()
            target = reply_msg.sender_id
        except:
            await ok.edit("» 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁 ʙᴏss 🙄 !!")
            return

        if str(target) in sudousers:
            newsudo = sudousers.replace(str(target), "").strip()
            await ok.edit(f"» 𝐅ʟ𝟒ᴍᴇ𝑋sᴘᴀᴍ 𝚄𝚂𝙴𝚁 𝚁𝙴𝙼𝙾𝚅𝙴𝙳\n\n🛠️ 𝙽𝙴𝚆 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁𝚂: {newsudo} 🛠️")
            heroku_var["SUDO_USERS"] = newsudo
        else:
            await ok.edit("» 𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝙸𝚂 𝙽𝙾𝚃 𝙰 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁 𝙱𝙾𝚂𝚂😪 !!")
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» 𝚂𝙾𝚁𝚁𝚈, 𝙾𝙽𝙻𝚈 𝚂𝚄𝙳𝙾 𝙲𝙰𝙽 𝚁𝙴𝙼𝙾𝚅𝙴 𝚂𝚄𝙳𝙾 𝚂𝙸𝚁😅.")
        
        
@X1.on(events.NewMessage(incoming=True, pattern=r"\%sudolist(?: |$)(.*)" % hl))
@X2.on(events.NewMessage(incoming=True, pattern=r"\%sudolist(?: |$)(.*)" % hl))
@X3.on(events.NewMessage(incoming=True, pattern=r"\%sudolist(?: |$)(.*)" % hl))
@X4.on(events.NewMessage(incoming=True, pattern=r"\%sudolist(?: |$)(.*)" % hl))
@X5.on(events.NewMessage(incoming=True, pattern=r"\%sudolist(?: |$)(.*)" % hl))
@X6.on(events.NewMessage(incoming=True, pattern=r"\%sudolist(?: |$)(.*)" % hl))
@X7.on(events.NewMessage(incoming=True, pattern=r"\%sudolist(?: |$)(.*)" % hl))
@X8.on(events.NewMessage(incoming=True, pattern=r"\%sudolist(?: |$)(.*)" % hl))
@X9.on(events.NewMessage(incoming=True, pattern=r"\%sudolist(?: |$)(.*)" % hl))
@X10.on(events.NewMessage(incoming=True, pattern=r"\%sudolist(?: |$)(.*)" % hl))
async def sudolist(event):
    if event.sender_id == OWNER_ID:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        sudousers = getenv("SUDO_USERS", default=None)

        if sudousers:
            await event.reply(f"» 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃: {sudousers}")
        else:
            await event.reply("» 𝙽𝙾 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁𝚂 𝙰𝚍𝚍𝚎𝚍.")
    
    elif event.sender_id in SUDO_USERS:
        await event.reply("» 𝚂𝙾𝚁𝚁𝚈, 𝙾𝙽𝙻𝚈 𝙾𝚆𝙽𝙴𝚁 𝙲𝙰𝙽 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙸𝚂 𝙲𝙾𝙼𝙼𝙰𝙽𝙳.")

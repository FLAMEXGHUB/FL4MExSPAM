from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("☞ 𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒 ☜", data="help_back")
    ],
    [
        Button.url("☞ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 ☜", "https://t.me/FL4ME_MAIN"),
        Button.url("☞ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 ☜", "https://t.me/FL4ME_CHATS")
    ],
    [
        Button.url("☞ 𝐓𝐇𝐄 𝐅ʟ𝟒ᴍᴇ ☜", "https://t.me/FL4ME_NETWORK")
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ℍ𝔼𝕐!🥀 [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\n𝕀 𝔸𝕄 [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **𝕄𝕐 𝕃𝕆ℝ𝔻✨ : [⚡𝗚𝗢𝗗 𝗡𝗘𝗢𝗡𝗘𝗫⚡](https://t.me/LORD_NEONEX_FL4ME)**\n\n"
        TEXT += f"» ** 𝐅ʟ𝟒ᴍᴇ𝑋sᴘᴀᴍ ᴠᴇʀsɪᴏɴ :** `M3.3`\n"
        TEXT += f"» **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `3.11.3`\n"
        TEXT += f"» **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://telegra.ph/file/386225057c825d3023789.mp4",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )

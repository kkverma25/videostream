# Copyright (C) 2021 By MarrkMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Welcome [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝑨𝖑𝖑𝖔𝖜𝖘  𝖄𝖔𝖚 𝖙𝖔 𝖕𝖑𝖆𝒚 𝖒𝖚𝖘𝖎𝖈 𝖆𝖓𝖉 𝒗𝖎𝖉𝖊𝖔 𝖔𝖓 𝖌𝖗𝖔𝖚𝖕𝖘 𝖙𝖍𝖗𝖔𝖚𝖌𝖍 𝖙𝖍𝖊 𝖓𝖊𝒘 𝖙𝖊𝖑𝖊𝖌𝖗𝖆𝖒'𝖘 𝖛𝖎𝖉𝖊𝖔 𝖈𝖍𝖆𝖙!!**

💡 **💡𝕱𝖎𝖓𝖉 𝖔𝖚𝖙 𝖆𝖑𝖑 𝖙𝖍𝖊 𝖇𝖔𝖙'𝖘  𝖆𝖓𝖉 𝖍𝖔𝒘 𝖙𝖍𝖊𝖞 𝒘𝖔𝖗𝖐 𝖇𝒚 𝖈𝖑𝖎𝖈𝖐𝖎𝖓𝖌 𝖔𝖓 𝖙𝖍𝖊  » 📚𝐂𝐌𝐃𝐒 𝖇𝖚𝖙𝖙𝖔𝖓!**

🔖 **🔖 𝖙𝖔 𝖐𝖓𝖔𝒘 𝖍𝖔𝒘 𝖙𝖔 𝖚𝖘𝖊 𝖙𝖍𝖎𝖘 𝖇𝖔𝖙, 𝖕𝖊𝖑𝖊𝖆𝖘𝖊 𝖈𝖑𝖎𝖈𝖐 𝖔𝖓 𝖙𝖍𝖊  » ❓ 𝐁𝐀𝐒𝐈𝐂 𝐆𝐔𝐈𝐃𝐄!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶🎶𝐀𝐃𝐃 𝐌𝐄🎶🎶",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("𝐁𝐀𝐒𝐈𝐂 𝐆𝐔𝐈𝐃𝐄", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚𝐂𝐌𝐃𝐒", callback_data="cbcmds"),
                    InlineKeyboardButton("𝐕𝐈𝐒𝐈𝐓 𝐇𝐄𝐑𝐄", url=f"https://t.me/About_EVERETT"),
                ],
                [
                    InlineKeyboardButton(
                        "🤴𝐃𝐄𝐕🤴", url=f"https://t.me/D_E_V_l_L"
                    ),
                    InlineKeyboardButton(
                        "🎧𝐌𝐔𝐒𝐈𝐂𝐒🎧", url=f"https://t.me/HINDI_MUS1C"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🎬𝐌𝐎𝐕𝐈𝐄𝐒🎬", url=f"https://t.me/backup_channel_000"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴀᴅᴍɪɴ ᴄᴍᴅ", callback_data="cbadmin"),
                    InlineKeyboardButton("sᴜᴅᴏ ᴄᴍᴅ", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("ʙᴀsɪᴄ ᴄᴍᴅ", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙ɢᴏ ʙᴀᴄᴋ", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

» /play (song name/link) - play music on video chat
» /stream (query/link) - stream the yt live/radio live music
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link

» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /leaveall - order userbot to leave from all group

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()

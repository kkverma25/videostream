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
        f"""✨ **𝒲ℯ𝓁𝒸ℴ𝓂ℯ [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝓪𝓵𝓵𝓸𝔀𝓼 𝔂𝓸𝓾 𝓽𝓸 𝓹𝓵𝓪𝔂 𝓶𝓾𝓼𝓲𝓬 𝓪𝓷𝓭 𝓿𝓲𝓭𝓮𝓸 𝓸𝓷 𝓰𝓻𝓸𝓾𝓹𝓼 𝓽𝓱𝓻𝓸𝓾𝓰𝓱 𝓽𝓱𝓮 𝓷𝓮𝔀 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶'𝓼 𝓿𝓲𝓭𝓮𝓸 𝓬𝓱𝓪𝓽𝓼!**
💡 **𝓕𝓲𝓷𝓭 𝓸𝓾𝓽 𝓪𝓵𝓵 𝓽𝓱𝓮 𝓑𝓸𝓽'𝓼 𝓬𝓸𝓶𝓶𝓪𝓷𝓭𝓼 𝓪𝓷𝓭 𝓱𝓸𝔀 𝓽𝓱𝓮𝔂 𝔀𝓸𝓻𝓴 𝓫𝔂 𝓬𝓵𝓲𝓬𝓴𝓲𝓷𝓰 𝓸𝓷 𝓽𝓱𝓮 » 📚𝒞ℴ𝓂𝓂𝒶𝓃𝒹𝓈 𝒷𝓊𝓉𝓉ℴ𝓃!**

🔖 **𝒯ℴ 𝓀𝓃ℴ𝓌 𝒽ℴ𝓌 𝓉ℴ 𝓊𝓈ℯ 𝓉𝒽𝒾𝓈 𝒷ℴ𝓉, 𝓅𝓁ℯ𝒶𝓈ℯ 𝒸𝓁𝒾𝒸𝓀 ℴ𝓃 𝓉𝒽ℯ » ❓ℬ𝒶𝓈𝒾𝒸 𝒢𝓊𝒾𝒹ℯ 𝒷𝓊𝓉𝓉ℴ𝓃!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ 𝕬𝖉𝖉 𝖒𝖊 𝖙𝖔 𝖞𝖔𝖚𝖗 𝕲𝖗𝖔𝖚𝖕 ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓𝙱𝚊𝚜𝚒𝚌 𝙶𝚞𝚒𝚍𝚎", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚𝙲𝚘𝚖𝚖𝚊𝚗𝚍𝚜", callback_data="cbcmds"),
                    InlineKeyboardButton("✨𝕱𝖆𝖙𝖍𝖊𝖗✨", url=f"https://t.me/marrk85"),
                ],
                [
                    InlineKeyboardButton(
                        "👥𝙶𝚛𝚘𝚞𝚙", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣𝙲𝚑𝚊𝚗𝚗𝚎𝚕", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐 𝑺𝒐𝒖𝒓𝒄𝒆 𝑪𝒐𝒅𝒆", url="https://github.com/marrk85/marrk-video-stream"
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
                    InlineKeyboardButton("👷🏻 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
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

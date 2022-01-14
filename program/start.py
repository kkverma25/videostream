from datetime import datetime
from sys import version_info
from time import time

from config import (
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.filters import command, other_filters
from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgQAAxkBAAEECP1hoQ3WiZmIgZ1M6zpI4tagFYi5AQACcQsAArp60VE-Obmr9D4hkiIE")
    await message.reply_text(
        f"""✨ **𝒲ℯ𝓁𝒸ℴ𝓂ℯ {message.from_user.mention()} !**\n
💭 [{BOT_NAME}](https://t.me/{BOT_USERNAME}) **𝓪𝓵𝓵𝓸𝔀𝓼 𝔂𝓸𝓾 𝓽𝓸 𝓹𝓵𝓪𝔂 𝓶𝓾𝓼𝓲𝓬 𝓪𝓷𝓭 𝓿𝓲𝓭𝓮𝓸 𝓸𝓷 𝓰𝓻𝓸𝓾𝓹𝓼 𝓽𝓱𝓻𝓸𝓾𝓰𝓱 𝓽𝓱𝓮 𝓷𝓮𝔀 𝓣𝓮𝓵𝓮𝓰𝓻𝓪𝓶'𝓼 𝓿𝓲𝓭𝓮𝓸 𝓬𝓱𝓪𝓽𝓼!**

💡 **𝓕𝓲𝓷𝓭 𝓸𝓾𝓽 𝓪𝓵𝓵 𝓽𝓱𝓮 𝓑𝓸𝓽'𝓼 𝓬𝓸𝓶𝓶𝓪𝓷𝓭𝓼 𝓪𝓷𝓭 𝓱𝓸𝔀 𝓽𝓱𝓮𝔂 𝔀𝓸𝓻𝓴 𝓫𝔂 𝓬𝓵𝓲𝓬𝓴𝓲𝓷𝓰 𝓸𝓷 𝓽𝓱𝓮 » 📚𝒞ℴ𝓂𝓂𝒶𝓃𝒹𝓈 𝒷𝓊𝓉𝓉ℴ𝓃!**

🔖 **𝒯ℴ 𝓀𝓃ℴ𝓌 𝒽ℴ𝓌 𝓉ℴ 𝓊𝓈ℯ 𝓉𝒽𝒾𝓈 𝒷ℴ𝓉, 𝓅𝓁ℯ𝒶𝓈ℯ 𝒸𝓁𝒾𝒸𝓀 ℴ𝓃 𝓉𝒽ℯ » ❓ℬ𝒶𝓈𝒾𝒸 𝒢𝓊𝒾𝒹ℯ 𝒷𝓊𝓉𝓉ℴ𝓃!**
""",
     photo=f"https://te.legra.ph/file/d9635c34298e74f348cfd.jpg",

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
                        "👥𝙶𝚛𝚘𝚞𝚙", url=f"https://t.me/marrkmusic"
                    ),
                    InlineKeyboardButton(
                        "📣𝙲𝚑𝚊𝚗𝚗𝚎𝚕", url=f"https://t.me/marrkchannel"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "🌐𝑺𝒐𝒖𝒓𝒄𝒆 𝑪𝒐𝒅𝒆", url="https://t.me/marrkmusic"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_message(
    command(["alive", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("✨ Group", url=f"https://t.me/marrkmusic"),
                InlineKeyboardButton(
                    "Official Channel", url=f"https://t.me/marrkchannel"
                ),
            ]
        ]
    )

    alive = f"**Hello {message.from_user.mention()}, i'm {BOT_NAME}**\n\n✨ Bot is working normally\n🍀 My Master: [IRON ♡](https://t.me/marrk85)\n✨ Bot Version: `v{__version__}`\n🍀 Pyrogram Version: `{pyrover}`\n✨ Python Version: `{__python_version__}`\n🍀 PyTgCalls version: `{pytover.__version__}`\n✨ Uptime Status: `{uptime}`\n\n**Thanks for Adding me here, for playing video & music on your Group video chat** ❤"

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("🏓 `PONG!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )

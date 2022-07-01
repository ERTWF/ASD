from modules.config import (
    START_PIC, 
    BOT_USERNAME,
    SUPPORT_GROUP,
    OWNER_USERNAME,
    UPDATES_CHANNEL,
)
from modules.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(
    command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"{START_PIC}",
        caption=f"""**💥 اهلا بك اختصاص هذا البوت 
تشغيل الاغاني في المكالمات الصوتية » 
لمعرفة الاوامر عليك النقر على زر الاوامر.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎯 ¦ اضـفـني الى مـجمـوعـتك ¦ 🎯",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ],
                [
                    InlineKeyboardButton("🥇 ¦ المـــطور", url=f"https://t.me/{OWNER_USERNAME}"),
                    InlineKeyboardButton("🖥 ¦ الأوامــر", url=f"https://telegra.ph/%F0%9D%99%B2%E1%B4%8F%E1%B4%8D%E1%B4%8D%E1%B4%80%C9%B4%E1%B4%85s-04-06"),
                ],
                [
                    InlineKeyboardButton(
                        "🥇 ¦ الــكروب", url=f"{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "⚙️ ¦ الـسـورس", url=f"{UPDATES_CHANNEL}"
                    ),
                ],
            ]
        ),
    )



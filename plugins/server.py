import os
import sys
from pyrogram.types import Message
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from os import system, execle, environ
from modules.helpers.decorators import sudo_users_only
from modules.config import BOT_USERNAME


@Client.on_message(commandpro(["R", "اعادة", "/restart@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def restart_bot(_, message: Message):
    msg = await message.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
    args = [sys.executable, "main.py"]
    await msg.edit("✅ جاري اعادة البوت\n✅ ستناني دقيقه وشغلني لاتستعجل")
    execle(sys.executable, *args, environ)
    return


import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
session_string = os.getenv("SESSION_STRING")

client = TelegramClient(StringSession(session_string), api_id, api_hash)

# ۱. دستور نمایش پنل راهنما
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.پنل\$'))
async def self_panel(event):
    panel_text = (
        "**🔥 به پنل پیشرفته سلف‌بات پالس خوش آمدید!**\n\n"
        "🔹 `.وضعیت` -> بررسی آنلاین بودن ربات\n"
        "🔹 `.پاکسازی [تعداد]` -> حذف پیام‌های شما در چت\n"
        "🔹 `.ایدی` -> دریافت آیدی عددی شما و چت فعلی\n"
        "🔹 `.سنجاق` -> سنجاق کردن پیام ریپلای شده\n"
        "🔹 `.زمان` -> نمایش ساعت رسمی سرور"
    )
    await event.edit(panel_text)

# ۲. دستور بررسی وضعیت
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.وضعیت\$'))
async def self_status(event):
    await event.edit("**سلف‌بات پالس با سرعت صدم ثانیه روی سرور ابری فعال است! 🚀⚡️**")

# ۳. دستور پاکسازی پیام‌ها
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.پاکسازی (\d+)\$'))
async def self_purge(event):
    count = int(event.pattern_match.group(1))
    await event.delete()
    async for msg in client.iter_messages(event.chat_id, limit=count, from_user='me'):
        await msg.delete()

# ۴. دستور دریافت آیدی
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.ایدی\$'))
async def self_id(event):
    await event.edit(f"**👤 آیدی شما:** `{event.sender_id}`\n**💬 آیدی این چت:** `{event.chat_id}`")

# ۵. دستور سنجاق کردن پیام
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.سنجاق\$'))
async def self_pin(event):
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        await reply_msg.pin()
        await event.edit("**📌 پیام با موفقیت سنجاق شد.**")
    else:
        await event.edit("**⚠️ لطفا این دستور را روی یک پیام ریپلای کنید!**")

print("سلف‌بات پالس آماده کار است!")
client.start()
client.run_until_disconnected()

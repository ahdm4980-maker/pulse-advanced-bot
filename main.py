import os
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# قرار دادن مستقیم اطلاعات سالم برای دور زدن کش سرور رندر
api_id = 25942287
api_hash = "90bd2c9fc548b905451a27c821d5db7"
session_string = "1BJWap1sBu0tBGz4fGeK9vCQeOqLlWhL9OVU2wLPojnQcc4iu9U0wHYH4oL4W1JN1FnCy7oXpA6h325PYj_aX12ACjDbPHpXMA9lui8pL83-OntiZLnerUMOQt3F9CZecTozhvyG_A9owHxA5tnqtXAgjp5m4bPtwdTwGJ_PSaaZujRuwGPfgxPRE7UT25M_ldYPSADjzluBw9AxXWf4yGsHsyGCvYKWbNgdhp-EV7pIX-el6oESKaBFBCobGAvEzqpMhx7BOeDoOHs0RurZEH3kgur4kREFTca5IXcLZc_fqxL--P8__bqxo8llNL3ma6lFPUa9D5im2JECe8BgdPuuyzFmBdsE="

client = TelegramClient(StringSession(session_string), api_id, api_hash)

# ۱. دستور نمایش پنل راهنما (فقط برای خودت)
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

# ۲. دستور بررسی وضعیت (فقط برای خودت)
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.وضعیت\$'))
async def self_status(event):
    await event.edit("**سلف‌بات پالس با سرعت صدم ثانیه روی سرور ابری فعال است! 🚀⚡️**")

# ۳. دستور پاکسازی پیام‌ها (فقط برای خودت)
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.پاکسازی (\d+)\$'))
async def self_purge(event):
    count = int(event.pattern_match.group(1))
    await event.delete()
    async for msg in client.iter_messages(event.chat_id, limit=count, from_user='me'):
        await msg.delete()

# ۴. دستور دریافت آیدی (فقط برای خودت)
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.ایدی\$'))
async def self_id(event):
    await event.edit(f"**👤 آیدی شما:** `{event.sender_id}`\n**💬 آیدی این چت:** `{event.chat_id}`")

# ۵. دستور سنجاق کردن پیام (فقط برای خودت)
@client.on(events.NewMessage(outgoing=True, pattern=r'^\.سنجاق\$'))
async def self_pin(event):
    if event.is_reply:
        reply_msg = await event.get_reply_message()
        await reply_msg.pin()
        await event.edit("**📌 پیام با موفقیت سنجاق شد.**")
    else:
        await event.edit("**⚠️ لطفا این دستور را روی یک پیام ریپلای کنید!**")

print("سلف‌بات پالس با موفقیت بدون کش سرور روشن شد!")
client.start()
client.run_until_disconnected()

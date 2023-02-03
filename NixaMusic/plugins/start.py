from NixaMusic import NixaMusic, BOT_USERNAME
from vars import vars
from telethon import events, Button

PM_START_TEXT = """
ʜᴇʏᴀ! {}
─────────────────────────
⦿ **ɪ'ᴍ ᴀ ꜱɪᴍᴘʟᴇ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴜꜱɪᴄ ᴀɴᴅ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ**.
⦿ **ɪ ᴄᴀɴ ᴘʟᴀʏ ꜱᴏɴɢꜱ ɪɴ ʏᴏᴜʀ ᴠᴏɪᴄᴇ**.
⦿ **ɪ ʜᴀᴠᴇ ᴀʟᴍᴏꜱᴛ ᴀʟʟ ꜰᴇᴀᴛᴜʀᴇꜱ ᴡʜɪᴄʜ ɴᴇᴇᴅꜱ ᴀ ᴍᴜꜱɪᴄ ʙᴏᴛ**
⦿ **ᴛʜɪꜱ ʙᴏᴛ ʙᴀꜱᴇᴅ ᴏɴ ᴛᴇʟᴇᴛʜᴏɴ. ꜱᴏ ɪᴛ'ꜱ ᴘʀᴏᴠɪᴅᴇ ᴍᴏʀᴇ ꜱᴛᴀʙɪʟɪᴛʏ ꜰʀᴏᴍ ᴏᴛʜᴇʀ ʙᴏᴛꜱ**!
⦿ **ɪ ᴄᴀɴ ᴅᴏ ᴏᴛʜᴇʀ ᴛʜɪɴɢꜱ ʟɪᴋᴇ ᴘɪɴꜱ ᴇᴛᴄ.**.
─────────────────────────
➠ **ᴄʟɪᴄᴋ ᴏɴ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ 🔘 ꜰᴏʀ ᴍᴏʀᴇ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ **.
"""

@NixaMusic.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ➕", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("📚 ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{vars.SUPPORT}"), Button.url("🍂 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{vars.CHANNEL}")],
        [Button.inline("📑 ᴄᴏᴍᴍᴀɴᴅꜱ", data="help"), Button.url("🎓 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/NixaXD")]])
       return

    if event.is_group:
       await event.reply("**ʜᴇʏ! ɪ'ᴍ ꜱᴛɪʟʟ ᴀʟɪᴠᴇ 😂**")
       return



@NixaMusic.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ ➕", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("📚 ꜱᴜᴘᴘᴏʀᴛ", f"https://t.me/{vars.SUPPORT}"), Button.url("🍂 ᴜᴘᴅᴀᴛᴇꜱ", f"https://t.me/{vars.CHANNEL}")],
        [Button.inline("📑 ᴄᴏᴍᴍᴀɴᴅꜱ", data="help"), Button.url("🎓 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/NixaXD")]])
       return

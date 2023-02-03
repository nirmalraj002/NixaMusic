from telethon import events, Button
from NixaMusic import NixMusic
from NixaMusic.status import *
import time
from vars import vars

PR_HELP = """
** ɴᴇᴇᴅ ᴛᴏ ᴅᴇʟᴇᴛᴇ ʟᴏᴛs ᴏғ ᴍᴇssᴀɢᴇs ? ᴛʜᴀᴛ's ᴡʜᴀᴛ ᴘᴜʀɢᴇs ᴀʀᴇ ғᴏʀ !**

‣ `/purge` - ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍsɢ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ᴛʜᴇʀᴇ.
‣ `/spurge` - sᴀᴍᴇ ᴀs ᴘᴜʀɢᴇ, ʙᴜᴛ ᴅᴏᴇs ɴᴏᴛ ᴛʜᴇ ғɪɴᴀʟ ᴄᴏɴғɪʀᴍᴀᴛɪᴏɴ ᴍᴇssᴀɢᴇs.
‣ `/del` - ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴍᴇssᴀɢᴇs.
"""

@NixaMusic.on(events.NewMessage(pattern=r"^[?!]purge"))
@is_admin
async def purge_messages(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.delete_messages:
         await event.reply(" ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs: ᴄᴀɴ ᴅᴇʟᴇʟᴛᴇ ᴍᴇssᴀɢᴇs.")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            " ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʟᴇᴄᴛ ᴡʜᴇʀᴇ ᴛᴏ sᴛᴀʀᴛ ᴘᴜʀɢɪɴɢ ғʀᴏᴍ.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)
    time_ = time.perf_counter() - start
    text = f"Purged in {time_:0.2f} Second(s)"
    await event.respond(text, parse_mode='markdown')

@NixaMusic.on(events.NewMessage(pattern="^[!?/]spurge"))
@is_admin
async def spurge(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.delete_messages:
         await event.reply("ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs: ᴄᴀɴ ᴅᴇʟᴇʟᴛᴇ ᴍᴇssᴀɢᴇs.")
         return
    start = time.perf_counter()
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply(
            "ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʟᴇᴄᴛ ᴡʜᴇʀᴇ ᴛᴏ sᴛᴀʀᴛ ᴘᴜʀɢɪɴɢ ғʀᴏᴍ.")
        return
    messages = []
    message_id = reply_msg.id
    delete_to = event.message.id

    messages.append(event.reply_to_msg_id)
    for msg_id in range(message_id, delete_to + 1):
        messages.append(msg_id)
        if len(messages) == 100:
            await event.client.delete_messages(event.chat_id, messages)
            messages = []

    await event.client.delete_messages(event.chat_id, messages)

@NixaMusic.on(events.NewMessage(pattern="^[!?/]del$"))
@is_admin
async def delete_messages(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.delete_messages:
       await event.reply("ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs: ᴄᴀɴ ᴅᴇʟᴇʟᴛᴇ ᴍᴇssᴀɢᴇs.")
       return
    msg = await event.get_reply_message()
    if not msg:
      await event.reply("ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ ᴅᴇʟᴇᴛᴇ.")
      return

    await msg.delete()
    await event.delete()

@NixaMusic.on(events.callbackquery.CallbackQuery(data="purges"))
async def _(event):
    await event.edit(PR_HELP, buttons=[[Button.inline("ʙᴀᴄᴋ", data="help")]])

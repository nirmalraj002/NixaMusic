from NixaMusic import NixaMusic
from NixaMusic.status import *
from vars import vars
from telethon import events, Button
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChatBannedRights

BANS_TEXT = """
** sᴏᴍᴇ ᴘᴇᴏᴘʟᴇ ɴᴇᴇᴅ ᴛᴏ ʙᴇ ᴘᴜʙʟɪᴄʟʏ ʙᴀɴɴᴇᴅ; sᴘᴀᴍᴍᴇʀ, ᴀɴɴᴏɴʏᴀɴᴄᴇs ᴏʀ ᴊᴜsᴛ ᴛʀᴏʟʟs.**

‣ `/kickme` - ᴛᴏ sᴇʟғ ᴋɪᴄᴋ ʏᴏᴜ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.
‣ `/kick` - ᴛᴏ ᴋɪᴄᴋ sᴏᴍᴇᴏɴᴇ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.
‣ `/unban` - ᴛᴏ ᴜɴʙᴀɴ ᴀ ᴍᴇᴍʙᴇʀ ғʀᴏᴍ ᴛʜᴇ ᴄʜᴀᴛ.
‣ `/ban` - ᴛᴏ ʙᴀɴ sᴏᴍᴇᴏɴᴇ ғʀᴏᴍ ᴀ ᴄʜᴀᴛ.
‣ `/dban` - ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴍsɢ ᴀɴᴅ ʙᴀɴs ᴛʜᴇ ᴜsᴇʀ.
‣ `/sban` - ᴛᴏ sɪʟᴇɴᴛ ʙᴀɴs ᴛʜᴇ ᴜsᴇʀs.
‣ `/skick` - ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴍsɢ ᴀɴᴅ ᴋɪᴄᴋs ᴛʜᴇ ᴜsᴇʀ. 
‣ `/dkick` - ᴛᴏ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴍsɢ ᴀɴᴅ ᴋɪᴄᴋs ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀs.
"""

@NixaMusic.on(events.NewMessage(pattern="^[!?/]kick ?(.*)"))
@is_admin
async def kick(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return

    if event.is_private:
        await event.reply("» ᴛʜɪs ᴄᴍᴅ ɪs ᴍᴀᴅᴇ ᴛᴏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs ɴᴏᴛ ᴘᴍ.")
        return
    if not perm.ban_users:
         await event.reply("» ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ: ᴄᴀɴ ʙᴀɴ ᴜsᴇʀs.")
         return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴏʀ ɢɪᴠᴇ ɪᴛs ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴋɪᴄᴋ ʜɪᴍ.")
        return

    replied_user = msg.sender_id
    us = msg.sender.username
    info = await Anon.get_entity(us)
    await Anon.kick_participant(event.chat_id, input_str or replied_user)
    await event.reply(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴋɪᴄᴋᴇᴅ [{info.first_name}](tg://user?id={replied_user}) ғʀᴏᴍ {event.chat.title}")

@NixaMusic.on(events.NewMessage(pattern="^[!?/]kickme"))
async def kickme(event):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
        await event.reply("» ᴛʜɪs ᴄᴍᴅ ɪs ᴍᴀᴅᴇ ᴛᴏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs ɴᴏᴛ ᴘᴍ.")
        return

    check = await Anon.get_permissions(event.chat_id, event.sender_id)
    if check.is_admin:
        await event.reply("sᴏʀʀʏ ʙᴜᴛ ɪ ᴄᴀɴ'ᴛ ᴋɪᴄᴋ ᴀᴅᴍɪɴs.")
        return

    await event.reply("ᴏᴋ, ᴀs ʏᴏᴜʀ ᴡɪsʜ")
    await Anon.kick_participant(event.chat_id, event.sender_id)

@NixaMusic.on(events.NewMessage(pattern="^[!?/]ban ?(.*)"))
@is_admin
async def ban(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
        await event.reply("» ᴛʜɪs ᴄᴍᴅ ɪs ᴍᴀᴅᴇ ᴛᴏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs ɴᴏᴛ ᴘᴍ.")
        return
    if not perm.ban_users:
        await event.reply("» ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ: ᴄᴀɴ ʙᴀɴ ᴜsᴇʀs.")
        return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴏʀ ɢɪᴠᴇ ɪᴛs ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ʙᴀɴ ʜɪᴍ")
        return
    replied_user = msg.sender_id
    us = msg.sender.username
    info = await NixaMusic.get_entity(us)
    await Anon(EditBannedRequest(event.chat_id, replied_user, ChatBannedRights(until_date=None, view_messages=True)))
    await event.reply(f"sᴜᴄᴄᴇssғᴜʟʟʏ ʙᴀɴɴᴇᴅ [{info.first_name}](tg://user?id={replied_user}) ɪɴ {event.chat.title}")

@NixaMusic.on(events.NewMessage(pattern="^[!?/]unban ?(.*)"))
@is_admin
async def unban(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if event.is_private:
        await event.reply("» ᴛʜɪs ᴄᴍᴅ ɪs ᴍᴀᴅᴇ ᴛᴏ ʙᴇ ᴜsᴇᴅ ɪɴ ɢʀᴏᴜᴘs ɴᴏᴛ ᴘᴍ.")
        return
    if not perm.ban_users:
        await event.reply("» ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ: ᴄᴀɴ ʙᴀɴ ᴜsᴇʀs.")
        return
    input_str = event.pattern_match.group(1)
    msg = await event.get_reply_message()
    if not input_str and not msg:
        await event.reply("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴏʀ ɢɪᴠᴇ ɪᴛs ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴜɴʙᴀɴ ʜɪᴍ")
        return
    replied_user = msg.sender_id
    us = msg.sender.username
    info = await NixaMusic.get_entity(us)
    await Anon(EditBannedRequest(event.chat_id, replied_user, ChatBannedRights(until_date=None, view_messages=False)))
    await event.reply(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴜɴʙᴀɴɴᴇᴅ [{info.first_name}](tg://user?id={replied_user}) ɪɴ {event.chat.title}")

@NixaMusic.on(events.NewMessage(pattern="^[!?/]skick"))
@is_admin
async def skick(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.ban_users:
         await event.reply("» ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ: ᴄᴀɴ ʙᴀɴ ᴜsᴇʀs.")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴏʀ ɢɪᴠᴇ ɪᴛs ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴋɪᴄᴋ ʜɪᴍ")
        return

    us = reply_msg.sender.username
    info = await Anon.get_entity(us)   
    x = (await event.get_reply_message()).sender_id
    zx = (await event.get_reply_message())
    await event.delete()
    await NixaMusic.kick_participant(event.chat_id, x)
    await event.reply(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴋɪᴄᴋᴇᴅ [{info.first_name}](tg://user?id={replied_user}) ғʀᴏᴍ {event.chat.title}")

@NixaMusic.on(events.NewMessage(pattern="^[!?/]dkick"))
@is_admin
async def dkick(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.ban_users:
         await event.reply("» ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ: ᴄᴀɴ ʙᴀɴ ᴜsᴇʀs.")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴏʀ ɢɪᴠᴇ ɪᴛs ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ᴋɪᴄᴋ ʜɪᴍ")
        return
    us = reply_msg.sender.username
    info = await Anon.get_entity(us) 
    x = await event.get_reply_message()
    await x.delete()
    await Anon.kick_participant(event.chat_id, x.sender_id)
    await event.reply(f"sᴜᴄᴄᴇssғᴜʟʟʏ ᴋɪᴄᴋᴇᴅ [{info.first_name}](tg://user?id={replied_user}) ғʀᴏᴍ {event.chat.title}")

@NixaMusic.on(events.NewMessage(pattern="^[!?/]dban"))
@is_admin
async def dban(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.ban_users:
         await event.reply("» ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ: ᴄᴀɴ ʙᴀɴ ᴜsᴇʀs.")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ ᴏʀ ɢɪᴠᴇ ɪᴛs ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ʙᴀɴ ʜɪᴍ")
        return
    us = reply_msg.sender.username
    info = await NixaMusic.get_entity(us) 
    x = (await event.get_reply_message()).sender_id
    zx = (await event.get_reply_message())
    await zx.delete()
    await NixaMusic(EditBannedRequest(event.chat_id, x, ChatBannedRights(until_date=None, view_messages=True)))
    await event.reply("sᴜᴄᴄᴇssғᴜʟʟʏ ʙᴀɴɴᴇᴅ !")
    await event.reply(f"sᴜᴄᴄᴇssғᴜʟʟʏ ʙᴀɴɴᴇᴅ [{info.first_name}](tg://user?id={replied_user}) ғʀᴏᴍ {event.chat.title}")

@NixaMusic.on(events.NewMessage(pattern="^[!?/]sban"))
@is_admin
async def sban(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.ban_users:
         await event.reply("» ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ: ᴄᴀɴ ʙᴀɴ ᴜsᴇʀs.")
         return
    reply_msg = await event.get_reply_message()
    if not reply_msg:
        await event.reply("» ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ sɪʟᴇɴᴛ ʙᴀɴ")
        return
    us = reply_msg.sender.username
    info = await NixaMusic.get_entity(us) 
    x = (await event.get_reply_message()).sender_id
    zx = (await event.get_reply_message())
    await event.delete()
    await NixaMusic(EditBannedRequest(event.chat_id, x, ChatBannedRights(until_date=None, view_messages=True)))
    await event.reply(f"sᴜᴄᴄᴇssғᴜʟʟʏ ʙᴀɴɴᴇᴅ [{info.first_name}](tg://user?id={replied_user}) ғʀᴏᴍ {event.chat.title}")

@NixaMusic.on(events.callbackquery.CallbackQuery(data="bans"))
async def banhelp(event):
    await event.edit(BANS_TEXT, buttons=[[Button.inline("ʙᴀᴄᴋ", data="help")]])

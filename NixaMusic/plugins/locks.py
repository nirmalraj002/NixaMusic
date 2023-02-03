from telethon import events, Button, types
from NixaMusic import NixaMusic
from NixaMusic.status import *
from vars import vars

LOCKS_HELP = """
** ᴅᴏ sᴛɪᴄᴋᴇʀs ᴀɴɴᴏʏ ʏᴏᴜ ? ᴏʀ ᴡᴀɴᴛ ᴛᴏ ᴀᴠᴏɪᴅ ᴘᴇᴏᴘʟᴇ sʜᴀʀɪɴɢ ʟɪɴᴋs ? ᴏʀ ᴘɪᴄᴛᴜʀᴇs ? ʏᴏᴜ'ʀᴇ ɪɴ ᴛʜᴇ ʀɪɢʜᴛ ᴘʟᴀᴄᴇ !**

‣ `/lock` - ᴛᴏ ʟᴏᴄᴋ ᴀ ᴍᴏᴅᴜʟᴇ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.
‣ `/unlock` - ᴛᴏ ᴜɴʟᴏᴄᴋ ᴀ ᴍᴏᴅᴜʟᴇ ɪɴ ᴛʜᴇ ᴄʜᴀᴛ.
‣ `/locktypes` - ᴛᴏ ɢᴇᴛ ᴀ ʟɪsᴛ ᴏғ ᴍᴏᴅᴜʟᴇs ᴄᴀɴ ʙᴇ ʟᴏᴄᴋᴇᴅ.
"""

@NixaMusic.on(events.NewMessage(pattern="^[!?/]lock ?(.*)"))
@is_admin
async def lock(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.change_info:
      await event.reply("ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs: ᴄᴀɴ ᴄʜᴀɴɢᴇ ɪɴғᴏ")
      return
    input_str = event.pattern_match.group(1)
    if not input_str:
       await event.reply("ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴘᴇᴄɪғɪᴇᴅ ᴀɴʏᴛʜɪɴɢ ᴛᴏ ʟᴏᴄᴋ.")
       return
    if "text" in input_str:
       await Stark.edit_permissions(event.chat_id, send_messages=False)
       await event.reply("ʟᴏᴄᴋᴇᴅ `ᴛᴇxᴛ`.")
    elif "media" in input_str:
       await Stark.edit_permissions(event.chat_id, send_media=False)
       await event.reply("ʟᴏᴄᴋᴇᴅ `ᴍᴇᴅɪᴀ`.")
    elif "sticker" in input_str:
       await Stark.edit_permissions(event.chat_id, send_stickers=False)
       await event.reply("ʟᴏᴄᴋᴇᴅ `sᴛɪᴄᴋᴇʀ`.")
    elif "gifs" in input_str:
       await Stark.edit_permissions(event.chat_id, send_gifs=False)
       await event.reply("ʟᴏᴄᴋᴇᴅ `ɢɪғs`.")
    elif "forward" in input_str:
       await Stark.edit_permissions(event.chat_id, forwards=False)
       await event.reply("ʟᴏᴄᴋᴇᴅ `ғᴏʀᴡᴀʀᴅ`.")
    elif "games" in input_str:
       await Stark.edit_permissions(event.chat_id, send_games=False)
       await event.reply("ʟᴏᴄᴋᴇᴅ `ɢᴀᴍᴇs`.")
    elif "inline" in input_str:
       await Stark.edit_permissions(event.chat_id, send_inline=False)
       await event.reply("ʟᴏᴄᴋᴇᴅ `ɪɴʟɪɴᴇ`.")
    elif "polls" in input_str:
       await Stark.edit_permissions(event.chat_id, send_polls=False)
       await event.reply("ʟᴏᴄᴋᴇᴅ `ᴘᴏʟʟs`.")
    elif "preview" in input_str:
       await Stark.edit_permissions(event.chat_id, embed_link_previews=False)
       await event.reply("ʟᴏᴄᴋᴇᴅ `ᴘʀᴇᴠɪᴇᴡ`.")
    elif "all" in input_str:
       await Anon.edit_permissions(event.chat_id,
          send_messages=False, 
          send_media=False,
          send_stickers=False,
          send_gifs=False,
          send_games=False,
          send_inline=False,
          send_polls=False,
          embed_link_previews=False)
       await event.reply("ʟᴏᴄᴋᴇᴅ `ᴀʟʟ`.")


@NixaMusic.on(events.NewMessage(pattern="^[!?/]unlock ?(.*)"))
@is_admin
async def unlock(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.change_info:
      await event.reply("ʏᴏᴜ ᴀʀᴇ ᴍɪssɪɴɢ ᴛʜᴇ ғᴏʟʟᴏᴡɪɴɢ ʀɪɢʜᴛs ᴛᴏ ᴜsᴇ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅs: ᴄᴀɴ ᴄʜᴀɴɢᴇ ɪɴғᴏ")
      return
    input_str = event.pattern_match.group(1)
    if not input_str:
       await event.reply("ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ sᴘᴇᴄɪғɪᴇᴅ ᴀɴʏᴛʜɪɴɢ ᴛᴏ ʟᴏᴄᴋ.")
       return
    if "text" in input_str:
       await Stark.edit_permissions(event.chat_id, send_messages=True)
       await event.reply("ᴜɴʟᴏᴄᴋᴇᴅ `ᴛᴇxᴛ`.")
    elif "media" in input_str:
       await Stark.edit_permissions(event.chat_id, send_media=True)
       await event.reply("ᴜɴʟᴏᴄᴋᴇᴅ `ᴍᴇᴅɪᴀ`.")
    elif "sticker" in input_str:
       await Stark.edit_permissions(event.chat_id, send_stickers=True)
       await event.reply("ᴜɴʟᴏᴄᴋᴇᴅ `sᴛɪᴄᴋᴇʀ`.")
    elif "gifs" in input_str:
       await Stark.edit_permissions(event.chat_id, send_gifs=True)
       await event.reply("ᴜɴʟᴏᴄᴋᴇᴅ `ɢɪғs`.")
    elif "forward" in input_str:
       await Stark.edit_permissions(event.chat_id, forwards=True)
       await event.reply("ᴜɴʟᴏᴄᴋᴇᴅ `ғᴏʀᴡᴀʀᴅ`.")
    elif "games" in input_str:
       await Stark.edit_permissions(event.chat_id, send_games=True)
       await event.reply("ᴜɴʟᴏᴄᴋᴇᴅ `ɢᴀᴍᴇs`.")
    elif "inline" in input_str:
       await Stark.edit_permissions(event.chat_id, send_inline=True)
       await event.reply("ᴜɴʟᴏᴄᴋᴇᴅ `ɪɴʟɪɴᴇ`.")
    elif "polls" in input_str:
       await Stark.edit_permissions(event.chat_id, send_polls=True)
       await event.reply("ᴜɴʟᴏᴄᴋᴇᴅ `ᴘᴏʟʟs`.")
    elif "preview" in input_str:
       await Stark.edit_permissions(event.chat_id, embed_link_previews=True)
       await event.reply("ᴜɴʟᴏᴄᴋᴇᴅ `ᴘʀᴇᴠɪᴇᴡ`.")
    elif "all" in input_str:
       await Anon.edit_permissions(event.chat_id,
          send_messages=True, 
          send_media=True,
          send_stickers=True,
          send_gifs=True,
          send_games=True,
          send_inline=True,
          send_polls=True,
          embed_link_previews=True)
       await event.reply("ᴜɴʟᴏᴄᴋᴇᴅ `ᴀʟʟ`.")


@NisthaMusic.on(events.NewMessage(pattern="^[!?/]locktypes"))
async def locktypes(event):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    TEXT = """
**ʟᴏᴄᴋs:**

‣ ᴛᴇxᴛ
‣ ᴍᴇᴅɪᴀ
‣ sᴛɪᴄᴋᴇʀ
‣ ɢɪғs
‣ ғᴏʀᴡᴀʀᴅ
‣ ᴘʀᴇᴠɪᴇᴡ
‣ ᴘᴏʟʟs
‣ ɢᴀᴍᴇs
‣ ɪɴʟɪɴᴇ 
‣ ᴀʟʟ
"""
    await event.reply(TEXT)

@NixaMusic.on(events.callbackquery.CallbackQuery(data="locks"))
async def _(event):

    await event.edit(LOCKS_HELP, buttons=[[Button.inline("ʙᴀᴄᴋ", data="help")]])

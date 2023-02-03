from telethon import events, Button
from NixaMusic import NixaMusic
from NixaMusic.status import *
from vars import vars
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@NixaMusic.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("ʙᴀᴄᴋ", data="help")]])

@NixaMusic.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("ʙᴀᴄᴋ", data="help")]])


ADMIN_TEXT = """
** ᴀ ᴍᴏᴅᴜʟᴇ ғʀᴏᴍ ᴡʜɪᴄʜ ᴀᴅᴍɪɴs ᴏғ ᴛʜᴇ ᴄʜᴀᴛ ᴄᴀɴ ᴜsᴇ.**

‣ `/end` - ᴛᴏ ᴇɴᴅ ᴍᴜsɪᴄ sᴛʀᴇᴀᴍɪɴɢ.
‣ `/skip` - ᴛᴏ sᴋɪᴘ ᴛʀᴀᴄᴋs ɢᴏɪɴɢ ᴏɴ.
‣ `/pause` - ᴛᴏ ᴘᴀᴜsᴇ sᴛʀᴇᴀᴍɪɴɢ.
‣ `/resume` - ᴛᴏ ʀᴇsᴜᴍᴇ sᴛʀᴇᴀᴍɪɴɢ.
‣ `/leavevc` - ғᴏʀᴄᴇ ᴛʜᴇ ᴜsᴇʀʙᴏᴛ ᴛᴏ ʟᴇᴀᴠᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.
‣ `/playlist` - ᴛᴏ ᴄʜᴇᴄᴋ ᴘʟᴀʏʟɪsᴛs.
"""

PLAY_TEXT = """
** ᴀ ᴍᴏᴅᴜʟᴇ ғʀᴏᴍ ᴡʜɪᴄʜ ᴜsᴇʀs ᴏғ ᴛʜᴇ ᴄʜᴀᴛ ᴄᴀɴ ᴜsᴇ.**

‣ `/play` - ᴛᴏ ᴘʟᴀʏ ᴀᴜᴅɪᴏ ғʀᴏᴍ ᴇʟsᴇ ʀᴇᴘʟʏ ᴛᴏ ᴀᴜᴅɪᴏ ғɪʟᴇ.
‣ `/vplay` - ᴛᴏ sᴛʀᴇᴀᴍ ᴠɪᴅᴇᴏ).
"""

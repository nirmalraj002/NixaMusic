import os
import sys
import random
from datetime import datetime
from os import execl
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from NixaMusic import *
from NixaMusic.status import *


@NixaMusic.on(events.NewMessage(pattern="^[!?/]userbotjoin ?(.*)"))
@is_admin
async def _(e, perm):
    chat_id = e.chat_id
    usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ᴊᴏɪɴ\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n/userbotjoin <ɢʀᴏᴜᴘ ʟɪɴᴋ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ> ɪғ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪs ᴘʀɪᴠᴀᴛᴇ ᴛʜᴇɴ ᴜsᴇ /pjoin <ᴄʜᴀᴛ ʟɪɴᴋ>"
    if e.is_group:
        dhoka = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 6:
            bc = dhoka[0]
            text = "ᴘʀᴏᴄᴇssɪɴɢ..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await client(functions.channels.JoinChannelRequest(channel=bc))
                await event.edit("» sᴜᴄᴄᴇssғᴜʟʟʏ ᴊᴏɪɴᴇᴅ ɪғ ɴᴏᴛ ᴊᴏɪɴᴇᴅ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅ /pjoin ᴀɴᴅ ʏᴏᴜʀ ɢʀᴏᴜᴘ ʟɪɴᴋ")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )


@NixaMusic.on(events.NewMessage(pattern="^[!?/]pjoin ?(.*)"))
@is_admin        
async def _(e, perm):
    chat_id = e.chat_id
    usage = "ᴍᴏᴅᴜʟᴇ ɴᴀᴍᴇ = ᴘʀɪᴠᴀᴛᴇ ᴊᴏɪɴ\n\nᴄᴏᴍᴍᴀɴᴅ:\n\n/pjoin <ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ ᴀᴄᴄᴇss ʜᴀsʜ>"
    if e.is_group:
        dhoka = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            invitelink = dhoka[0]
            text = "ᴘʀᴏᴄᴇssɪɴɢ..."
            event = await e.reply(text, parse_mode=None, link_preview=None )
            try:
                await client(ImportChatInviteRequest(invitelink))
                await event.edit("» ᴀssɪsᴛᴀɴᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ᴊᴏɪɴᴇᴅ...")
            except Exception as e:
                await event.edit(str(e))   
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
            
    

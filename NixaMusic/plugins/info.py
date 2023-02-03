from telethon import events, Button, types
from NixaMusic import NixaMusic
from NixaMusic.status import *
from vars import vars
from telethon.tl.types import ChannelParticipantsAdmins
from datetime import timedelta
from telethon.tl.functions.photos import GetUserPhotosRequest as P
from telethon.tl.functions.users import GetFullUserRequest


MISC_HELP = """
** ᴀɴ "ᴏᴅᴅs ᴀɴᴅ ᴇɴᴅs" ᴍᴏᴅᴜʟᴇ ғᴏʀ sᴍᴀʟʟ, sɪᴍᴘʟᴇ ᴄᴏᴍᴍᴀɴᴅs ᴡʜɪᴄʜ ᴅᴏɴ'ᴛ ʀᴇᴀʟʟʏ ғɪᴛ ᴀɴʏᴡʜᴇʀᴇ.**

‣ `/id` - ᴛᴏ ɢᴇᴛ ᴄᴜʀʀᴇɴᴛ ᴄʜᴀᴛ ɪᴅ ᴏʀ ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ.
‣ `/info` - ᴛᴏ ɢᴇᴛ ɪɴғᴏ ᴏғ ᴀ ᴜsᴇʀ.
"""

@NixaMusic.on(events.NewMessage(pattern="^[!?/]id"))
async def id(event):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return

    if event.is_private:
       await event.reply(f"ʏᴏᴜʀ ɪᴅ ɪs `{event.sender_id}`.")
       return

    ID = """
**ᴄʜᴀᴛ-ɪᴅ:** `{}`
**ᴜsᴇʀ-ɪᴅ:** `{}`
"""

    msg = await event.get_reply_message()
    if not msg:
      await event.reply(ID.format(event.chat_id, event.sender_id))
      return

    await event.reply(f"User {msg.sender.first_name} id is `{msg.sender_id}`.")
 
@NixaMusic.on(events.NewMessage(pattern="^[!?/]info ?(.*)"))
async def info(event):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    sed = await Anon(P(user_id=event.sender_id, offset=42, max_id=0, limit=80))
    hn = await Anon(GetFullUserRequest(event.sender_id))
    text = "**» ᴜsᴇʀ ɪɴғᴏ:**\n\n"
    text += "**» ғɪʀsᴛ ɴᴀᴍᴇ:** {}\n"
    text += "**» ʟᴀsᴛ ɴᴀᴍᴇ:** {}\n"
    text += "**» ᴜsᴇʀ-ɪᴅ:** `{}`\n"
    text += "**» ᴜsᴇʀɴᴀᴍᴇ:** @{}\n"
    text += "**» ɴᴏ. ᴏғ ᴘғᴘs:** `{}`\n"
    text += "**» ᴜsᴇʀ-ʙɪᴏ:** `{}`\n"
    text += "**» ᴘᴇʀᴍᴀʟɪɴᴋ:** [Link](tg://user?id={})\n"

    input_str = event.pattern_match.group(1)
    if not input_str:
          await Anon.send_message(event.chat_id, text.format(hn.user.first_name, hn.user.last_name, event.sender_id, event.sender.username, sed.count, hn.about, event.sender_id))
          return
 
    input_str = event.pattern_match.group(1)
    ha = await Anon.get_entity(input_str)
    hu = await NixaMusic(GetFullUserRequest(id=input_str))
    sedd = await NixaMusic(P(user_id=input_str, offset=42, max_id=0, limit=80))

    textn = "**» ᴜsᴇʀ ɪɴғᴏ:**\n\n"
    textn += "**» ғɪʀsᴛ ɴᴀᴍᴇ:** {}\n"
    textn += "**» ʟᴀsᴛ ɴᴀᴍᴇ:** {}\n"
    textn += "**» ᴜsᴇʀ-ɪᴅ:** `{}`\n"
    textn += "**» ᴜsᴇʀɴᴀᴍᴇ:** @{}\n"
    textn += "**» ɴᴏ. ᴏғ ᴘғᴘs:** `{}`\n"
    textn += "**» ᴜsᴇʀ-ʙɪᴏ:** `{}`\n"
    textn += "**» ᴘᴇʀᴍᴀLɪɴᴋ:** [Link](tg://user?id={})\n"

    await event.reply(textn.format(ha.first_name, ha.last_name, ha.id, ha.username, sedd.count, hu.about, ha.id))
   

@NixaMusic.on(events.callbackquery.CallbackQuery(data="misc"))
async def _(event):
    await event.edit(MISC_HELP, buttons=[[Button.inline("ʙᴀᴄᴋ", data="help")]])

from telethon import events, Button
from telethon.errors import ChatAdminRequiredError, UserAdminInvalidError
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsAdmins, ChatBannedRights
from NixaMusic import NixaMusic
from NixaMusic.status import *
from vars import vars

CLEANER_HELP = """
** ᴛʜɪs ɪs ᴀ ᴍᴏᴅᴜʟᴇ ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ғʀᴏᴍ ʏᴏᴜʀ ɢʀᴏᴜᴘs !**

‣ `?zombies` - ᴛᴏ ғɪɴᴅ ᴢᴏᴍʙɪᴇs ᴀᴄᴄᴏᴜɴᴛs ᴀᴄᴄᴏᴜɴᴛs ɪɴ ʏᴏᴜʀ ᴄʜᴀᴛ.
‣ `?zombies clean` - ᴛᴏ ʀᴇᴍᴏᴠᴇ ᴛʜᴇ ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ғʀᴏᴍ.
"""


BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)


@NixaMusic.on(events.NewMessage(pattern="^[!?/]zombies ?(.*)"))
@is_admin
async def clean(event, perm):
    if vars.MANAGEMENT_MODE == "ENABLE":
        return
    if not perm.ban_users:
      await event.reply("ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ᴇɴᴏᴜɢʜ ʀɪɢʜᴛs.")
      return
    input_str = event.pattern_match.group(1)
    stats = "Group is clean."
    deleted = 0

    if "clean" not in input_str:
      zombies = await event.respond("sᴇᴀʀᴄʜɪɴɢ ғᴏʀ ᴢᴏᴍʙɪᴇs /ᴅᴇʟᴇᴛᴇ ᴀᴄᴄᴏᴜɴᴛs...")
      async for user in event.client.iter_participants(event.chat_id):

            if user.deleted:
                deleted += 1
      if deleted > 0:
            stats = f"ғᴏᴜɴᴅ **{deleted}** ᴢᴏᴍʙɪᴇs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.\
            \nᴄʟᴇᴀɴ ᴛʜᴇᴍ ʙʏ ᴜsɪɴɢ - `/zombies clean`"
      await zombies.edit(stats)
      return

    cleaning_zombies = await event.respond("ᴀʟʟ ᴍɪɢʜᴛʏ ᴘᴜsʜ \n ᴄʟᴇᴀɴɪɴɢ ᴢᴏᴍʙɪᴇs /ᴅᴇʟᴇᴛᴇᴅ ᴀᴄᴄᴏᴜɴᴛs ...")
    del_u = 0
    del_a = 0

    async for user in event.client.iter_participants(event.chat_id):
        if user.deleted:
            try:
                await event.client(
                    EditBannedRequest(event.chat_id, user.id, BANNED_RIGHTS)
                )
            except ChatAdminRequiredError:
                await cleaning_zombies.edit("ɪ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʙᴀɴ ʀɪɢʜᴛs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ.")
                return
            except UserAdminInvalidError:
                del_u -= 1
                del_a += 1
            await event.client(EditBannedRequest(event.chat_id, user.id, UNBAN_RIGHTS))
            del_u += 1

    if del_u > 0:
        stats = f"ᴄʟᴇᴀɴᴇᴅ `{del_u}` ᴢᴏᴍʙɪᴇs"

    if del_a > 0:
        stats = f"ᴄʟᴇᴀɴᴇᴅ `{del_u}` ᴢᴏᴍʙɪᴇs \
        \n`{del_a}` ᴢᴏᴍʙɪᴇs ᴀᴅᴍɪɴ ᴀᴄᴄᴏᴜɴᴛs ᴀʀᴇ ɴᴏᴛ ʀᴇᴍᴏᴠᴇᴅ !"

    await cleaning_zombies.edit(stats)

@NixaMusic.on(events.callbackquery.CallbackQuery(data="zombies"))
async def _(event):
    await event.edit(CLEANER_HELP, buttons=[[Button.inline(" ʙᴀᴄᴋ ", data="help")]])

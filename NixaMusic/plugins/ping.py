import os
from telethon import Button, events
from NixaMusic import *

IMG = os.environ.get(
    "PING_PIC", "https://te.legra.ph/file/899e50f653c019748c90e.jpg"
)
ms = 501.455

ALIVE = os.environ.get(
    "ALIVE", "[sᴜᴍɪᴛ ʏᴀᴅᴀᴠ](https://t.me/Simple_Munda)"
)

CAPTION = f"**ᴘ ᴏ ɴ ɢ !**\n\n   » {ms}\n   » ᴍʏ ᴍᴀsᴛᴇʀ ~ {ALIVE}"


@NixaMusic.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    bsdk = [[
             Button.url("sᴜᴘᴘᴏʀᴛ", url="https://t.me/Hindi_English_Chatt"),
             Button.url("ᴜᴘᴅᴀᴛᴇs", url="https://t.me/Fake_Peoples")
                       ]]
    await Anon.send_file(event.chat_id, IMG, caption=CAPTION, buttons=bsdk)

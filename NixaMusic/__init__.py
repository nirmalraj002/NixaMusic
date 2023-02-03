  import os

from telethon import TelegramClient
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged
import logging
from pytgcalls import PyTgCalls
from telethon.network.connection.tcpabridged import ConnectionTcpAbridged

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)


from vars import vars
BOT_USERNAME = vars.BOT_USERNAME
ASSISTANT_ID = []

bot = TelegramClient('NixaMusic', api_id=vars.API_ID, api_hash=vars.API_HASH)
NixaMusic = bot.start(bot_token=vars.BOT_TOKEN)
client = TelegramClient(StringSession(vars.STRING_SESSION), vars.API_ID, vars.API_HASH)
call_py = PyTgCalls(client)
client.start()
call_py.start()

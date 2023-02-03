import asyncio
from NixaMusic import call_py, client
from vars import vars
from telethon.tl.functions.channels import LeaveChannelRequest

AUTO_LEAVE_TIME = vars.AUTO_LEAVE_TIME
AUTO_LEAVE = vars.AUTO_LEAVE

async def leave_from_inactive_call():
  if AUTO_LEAVE == True:
   while not await asyncio.sleep(AUTO_LEAVE_TIME):
    all_chat_id = []
    async for chat in client.iter_dialogs():
        chat_id = chat.id
        if chat_id != -1001847056948:
          if chat.is_group:
            for call in call_py.calls:
                call_chat_id = int(getattr(call, "chat_id"))
                if call_chat_id in all_chat_id:
                    pass
                else:
                    all_chat_id.append(call_chat_id)
                call_status = getattr(call, "status")
                try:
                    if call_chat_id == chat_id and call_status == "not_playing":
                        await client(LeaveChannelRequest(chat_id))
                    elif chat_id not in all_chat_id:
                        await client(LeaveChannelRequest(chat_id))
                except Exception:
                    pass
            if chat_id not in all_chat_id:
                try:
                    await client(LeaveChannelRequest(chat_id))
                except Exception:
                    pass

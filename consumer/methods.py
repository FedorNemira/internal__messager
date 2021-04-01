import asyncio
import json
import pprint
import aiohttp
from simple_print.functions import sprint_f
from settings import TELEGRAM_API_KEY

async def ping_pong(request):
    pprint.pprint(request)
    return


async def telegram_send_message(request):
    # {"chat_id": "218865388", "text": "adfsdf"}

    sprint_f(f"{request}")
    API_URL = "https://api.telegram.org/bot%s/sendMessage" % TELEGRAM_API_KEY

    headers = {"Content-Type": "application/json"}

    message = {"chat_id": request["chat_id"], "text": request["text"]}  # "218865388", # 813499020 , 831499020 , 111859928

    loop = asyncio.get_event_loop()
    resp = ""
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.post(API_URL, data=json.dumps(message), headers=headers) as response:
            if response.status == 200:
                pass
    return 1

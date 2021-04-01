
import pprint
import pytest
from ..consumer import methods


@pytest.mark.asyncio
async def test_telegram_send_message():
    json_rq = {"chat_id": "218865388", "text": "Makar vipil ROM, VODKA, VISKI and IMPER!"}
    pprint.pprint(json_rq)
    result = await methods.telegram_send_message(json_rq)
    assert result

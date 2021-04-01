from consumer import methods
from consumer import schema
from consumer.helpers import validate_request_schema


async def simple_message(message):
    print("Simple message body is: %r" % message.body)
    await message.channel.basic_ack(message.delivery.delivery_tag)


@validate_request_schema(schema.PingHost)
async def ping_pong(request):
    response = await methods.ping_pong(request)
    return response


@validate_request_schema(schema.TelegramSendMessage)
async def telegram_send_message(request):
    response = await methods.telegram_send_message(request)
    return response

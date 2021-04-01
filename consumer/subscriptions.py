import aiormq
from termcolor import cprint

from consumer import handlers
from settings import AMQP_URI


async def consumer_subscriptions():
    connection = await aiormq.connect(AMQP_URI)
    channel = await connection.channel()
    cprint("AMQP CONSUMER:     ready [yes]", "green")

    # declare queues
    simple_message__declared = await channel.queue_declare("reminder24:internal__messager:test_message")
    ping_pong__declared = await channel.queue_declare("reminder24:internal__messager:ping_pong")
    telegram_send_message__declared = await channel.queue_declare("reminder24:internal__messager:telegram_send_message")

    # bind handlers
    await channel.basic_consume(simple_message__declared.queue, handlers.simple_message, no_ack=True)
    await channel.basic_consume(ping_pong__declared.queue, handlers.ping_pong)
    await channel.basic_consume(telegram_send_message__declared.queue, handlers.telegram_send_message)

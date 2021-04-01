from aio_pika import connect_robust
from aio_pika.patterns import RPC
from termcolor import cprint

from rpc import methods
from settings import AMQP_URI


async def rpc_subscriptions():

    connection = await connect_robust(
        AMQP_URI,
    )

    channel = await connection.channel()

    rpc = await RPC.create(channel)
    await rpc.register("reminder24__upper_word__internal_messager", methods.upper_word__internal_messager, auto_delete=True)
    
    cprint("AMQP RPC:          ready [yes]", "green")
    return connection

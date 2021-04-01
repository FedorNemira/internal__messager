import datetime

import asyncpg
from simple_print.functions import sprint_f

from settings import DATABASE_URI


async def insert_monitor_activity(monitor_id, connection_established, response_time, test=False):
    sprint_f(f"monitor_id = {monitor_id} :: connection_established= {connection_established} :: response_time = {response_time}", "yellow")

    connection_established = str(connection_established).lower()

    response_time = round(response_time, 6)
    response_seconds, response_microseconds = str(response_time).split(".")
    if len(response_seconds) == 1:
        response_seconds = f"0{response_seconds}"
    response_time = f"00:00:{response_seconds}.{response_microseconds}"

    creation_date = datetime.datetime.now()

    conn = await asyncpg.connect(DATABASE_URI)

    insert_monitor_activity_record = f"""  
    INSERT INTO "monitoring_monitoractivity" 
    ("monitor_id", "connection_establish", "response_time", "creation_date") 
    VALUES ({monitor_id}, {connection_established}, '{response_time}'::time, '{creation_date}'::timestamptz) 
    """
    sprint_f(insert_monitor_activity_record, "cyan")
    try:
        status = await conn.execute(insert_monitor_activity_record)
        sprint_f(status, "red")
    except:
        pass
    finally:
        await conn.close()

    return 1

import asyncio

from utils.db_api.db_database import Database


async def test():
    db = Database()
    await db.create()
    await db.drop_users()
    print("Done")


asyncio.get_event_loop().run_until_complete(test())

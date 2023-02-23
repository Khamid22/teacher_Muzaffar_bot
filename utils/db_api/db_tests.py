import asyncio
from utils.db_api.db_database import Database


async def test():
    db = Database()
    await db.create()
    await db.create_table_products()

    await db.delete_products()
    await db.drop_products()

asyncio.get_event_loop().run_until_complete(test())


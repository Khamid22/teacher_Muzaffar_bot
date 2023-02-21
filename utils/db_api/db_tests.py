import asyncio

from utils.db_api.db_database import Database


async def test():
    db = Database()
    await db.create()
    await db.create_table_products()
    await db.create_table_users()

    customers = await db.select_all_users()
    products = await db.select_all_products()

    for customer in customers:
        print(customer)

    for product in products:
        print(product)

asyncio.get_event_loop().run_until_complete(test())

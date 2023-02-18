import asyncio

from utils.db_api.db_database import Database


async def test():
    db = Database()
    await db.create()
    await db.drop_users()
    print("Creating the users table")
    # await db.drop_users()
    await db.create_table_users()
    print("Done!")

    print("Let's add someone")
    await db.add_user("John", "JohnDoe", 9)
    print("Added")
    users = await db.select_all_users()




asyncio.get_event_loop().run_until_complete(test())
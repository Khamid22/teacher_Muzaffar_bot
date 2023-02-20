import asyncio

from utils.db_api.db_database import Database


async def test():
  db = Database()
  await db.create()
  await db.drop_users()
  print("Creating the users table")
  await db.create_table_users()
  print("Done!")

  print("Let's add someone")
  await db.add_user("John", "JohnDoe", 9)
  print("Added")
  await db.update_user_number(123123123, 9)
  print("Phone number updated successfully")
  await db.create_table_products()
  print("The table products have been created")


asyncio.get_event_loop().run_until_complete(test())

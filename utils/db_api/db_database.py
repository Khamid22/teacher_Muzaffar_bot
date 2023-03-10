from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:

  def __init__(self):
    self.pool: Union[Pool, None] = None

  async def create(self):
    self.pool = await asyncpg.create_pool(
      user=config.DB_USER,
      password=config.DB_PASS,
      host=config.DB_HOST,
      database=config.DB_NAME
    )

  async def execute(self, command, *args,
                    fetch: bool = False,
                    fetchval: bool = False,
                    fetchrow: bool = False,
                    execute: bool = False
                    ):
    async with self.pool.acquire() as connection:
      connection: Connection
      async with connection.transaction():
        if fetch:
          result = await connection.fetch(command, *args)
        elif fetchval:
          result = await connection.fetchval(command, *args)
        elif fetchrow:
          result = await connection.fetchrow(command, *args)
        elif execute:
          result = await connection.execute(command, *args)
      return result

  async def create_table_users(self):
    sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE,
        phone_number BIGINT NULL
        );
        """
    await self.execute(sql, execute=True)

  @staticmethod
  def format_args(sql, parameters: dict):
    sql += " AND ".join([
      f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
        start=1)
    ])
    return sql, tuple(parameters.values())

  async def add_user(self, full_name, username, telegram_id):
    sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
    return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

  async def update_user_number(self, phone_number, telegram_id):
    sql = "UPDATE Users SET phone_number=$1 WHERE telegram_id=$2"
    return await self.execute(sql, phone_number, telegram_id, execute=True)

  async def select_all_users(self):
    sql = "SELECT * FROM Users"
    async with self.pool.acquire() as conn:
      async with conn.transaction():
        results = await conn.fetch(sql)
        return [dict(r) for r in results]

  async def select_user(self, **kwargs):
    sql = "SELECT * FROM Users WHERE "
    sql, parameters = self.format_args(sql, parameters=kwargs)
    return await self.execute(sql, *parameters, fetchrow=True)

  async def count_users(self):
    sql = "SELECT COUNT(*) FROM Users"
    return await self.execute(sql, fetchval=True)

  async def update_user_username(self, username, telegram_id):
    sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
    return await self.execute(sql, username, telegram_id, execute=True)

  async def update_location(self, location, telegram_id):
    sql = "UPDATE Users SET location=$1 WHERE telegram_id=$2"
    return await self.execute(sql, location, telegram_id, execute=True)

  async def delete_users(self):
    await self.execute("DELETE FROM Users WHERE TRUE", execute=True)

  async def drop_users(self):
    await self.execute("DROP TABLE Users", execute=True)

  async def create_table_products(self):
    sql = """
        CREATE TABLE IF NOT EXISTS products(
        id SERIAL PRIMARY KEY,
        category_name VARCHAR(30) NOT NULL,
        product_name VARCHAR(50) NOT NULL,
        photo VARCHAR(200) NOT NULL,
        price BIGINT NOT NULL
        );
    """
    await self.execute(sql, execute=True)

  async def add_product(self, category_name, product_name, photo, price=None):
    sql = "INSERT INTO Products (category_name, product_name, photo, price) VALUES($1, $2, $3, $4) returning *"
    return await self.execute(sql, category_name, product_name, photo, price, fetchrow=True)

  async def select_all_products(self):
    sql = "SELECT * FROM products"
    async with self.pool.acquire() as conn:
      async with conn.transaction():
        results = await conn.fetch(sql)
        return [dict(r) for r in results]

  async def get_categories(self):
    sql = "SELECT DISTINCT category_name FROM Products"
    categories = await self.execute(sql, fetch=True)
    return [category['category_name'] for category in categories]

  async def get_products(self, category_name):
    sql = f"SELECT * FROM products WHERE category_name='{category_name}'"
    async with self.pool.acquire() as conn:
      async with conn.transaction():
        results = await conn.fetch(sql)
        return [dict(r) for r in results]

  async def drop_products(self):
    await self.execute("DROP TABLE Products", execute=True)

  async def delete_products(self):
    await self.execute("DELETE FROM Products WHERE TRUE", execute=True)



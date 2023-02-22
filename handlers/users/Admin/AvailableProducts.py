from loader import dp, db
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


@dp.message_handler(text="Available Products")
async def all_existing_products(message: Message):
    products = await db.select_all_products()

    page_size = 10
    page_number = 1
    if not products:
        await message.answer("<b>No registered products.</b>")
    else:
        start_index = (page_number - 1) * page_size
        end_index = start_index + page_size
        paginated_products = products[start_index:end_index]
        product_list = []
        for product in paginated_products:
            product_name = product.get("product_name")
            price = product.get("price")
            category_name = product.get("category_name")
            product_list.append(f"Category: {category_name}\nProduct: {product_name}\nPrice: {price}")

        result = "\n\n".join(product_list)

        prev_button = InlineKeyboardButton(
            "<< Prev",
            callback_data=f"product_list_page_{page_number - 1}"
        )

        next_button = InlineKeyboardButton(
            "Next >>",
            callback_data=f"product_list_page_{page_number + 1}"
        )

        keyboard = InlineKeyboardMarkup().add(prev_button, next_button)
        await message.answer(result, reply_markup=keyboard)


@dp.callback_query_handler(lambda c: c.data and c.data.startswith("product_list_page"))
async def process_callback_button(call: CallbackQuery):
    data = call.data
    page_number = int(data.split("_")[-1])
    products = await db.select_all_products()
    page_size = 10
    start_index = (page_number - 1) * page_size
    end_index = start_index + page_size
    paginated_products = products[start_index:end_index]
    product_list = []
    for product in paginated_products:
        product_name = product.get("product_name")
        price = product.get("price")
        category_name = product.get("category_name")
        product_list.append(f"Category: {category_name}\nProduct: {product_name}\nPrice: {price}")

    result = "\n\n".join(product_list)

    prev_button = InlineKeyboardButton(
        "<< Prev",
        callback_data=f"product_list_page_{page_number - 1}"
    )

    next_button = InlineKeyboardButton(
        "Next >>",
        callback_data=f"product_list_page_{page_number + 1}"
    )

    keyboard = InlineKeyboardMarkup().add(prev_button, next_button)
    await call.message.edit_text(result, reply_markup=keyboard)
    await call.answer()
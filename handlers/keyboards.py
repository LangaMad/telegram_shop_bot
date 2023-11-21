from aiogram.types import (ReplyKeyboardMarkup,
                           InlineKeyboardButton,
                           KeyboardButton,
                           InlineKeyboardMarkup,)
from aiogram.utils.keyboard import ReplyKeyboardBuilder,InlineKeyboardBuilder
from databases.request import get_categories , get_product,get_products

main_k = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Категории')],
    [KeyboardButton(text='Контакты')]
], resize_keyboard=True,input_field_placeholder='Выберите пункт')

async def categories():
    categories_kb = InlineKeyboardBuilder()
    categories = await get_categories()
    for category in categories:
        categories_kb.add(InlineKeyboardButton(text=category.name,
                    callback_data=f'category_{category.id}'))
    return categories_kb.adjust(2).as_markup()


async def product(category_id):
    product_kb = InlineKeyboardBuilder()
    product = await get_products(category_id)
    for products in product:
        product_kb.add(InlineKeyboardButton(text=products.name,
                    callback_data=f'product_{products.id}'))
    return product_kb.adjust(2).as_markup()


from aiogram import Router,F,Bot
from aiogram.filters import CommandStart
from aiogram.types import Message,CallbackQuery,FSInputFile
import handlers.keyboards as KB
from databases.request import get_product
from io import BytesIO
from PIL import Image
from config import TOKEN


bot = Bot(TOKEN)

router = Router()


@router.message(CommandStart())
async def get_start(message: Message):
    await message.answer("Здавствуйте,я бот магазин",reply_markup=KB.main_k)
    
    
@router.message(F.text == 'Категории')
async def category(message: Message):
    await message.answer('Выберите категорию телефона',
                    reply_markup=await KB.categories())

@router.callback_query(F.data.startswith('category_'))
async def category_select(callback: CallbackQuery):
    category_id = callback.data.split('_')[1]
    await callback.message.answer(f'Товары по этой катеогрии ', 
        reply_markup=await KB.product(category_id=category_id))
    await callback.answer("Вы Выбрали")

@router.callback_query(F.data.startswith('product_'))
async def product_select(callback: CallbackQuery):
    
    product_id = callback.data.split('_')[1]
    product = await get_product(product_id=product_id)
    photo = FSInputFile(product.image)
    await bot.send_photo(callback.message.chat.id,photo,caption=f'{product.name},\n {product.price}')
    # await callback.message.answer_photo(f'Вы выбрали товар {product.}')
    await callback.answer("Выбор")
    









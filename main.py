from aiogram import Bot, Dispatcher
import sys
import logging
from handlers.handlers import router
from config import TOKEN
import asyncio
from aiogram import F
from databases.models import async_main



async def main():
    await async_main()
    
    bot = Bot(TOKEN)
    dp = Dispatcher()
    dp.include_router(router=router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
    

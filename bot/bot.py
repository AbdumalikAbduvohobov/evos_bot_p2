import asyncio
from os import getenv

from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
from commands import router as commands_router
from handlers import router as handlers_router
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()

dp.include_router(commands_router)
dp.include_router(handlers_router)

# Run the bot
async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Starting bot...")
    asyncio.run(main())

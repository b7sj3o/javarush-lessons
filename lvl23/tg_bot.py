import asyncio
import time
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart



bot = Bot(token=token)
dp = Dispatcher()


async def gen_count(n: int):
    for i in range(1, n + 1):
        await asyncio.sleep(1)
        yield i

@dp.message(CommandStart())
async def start_command(message):
    async for value in gen_count(4):
        await message.answer(f"отримано: {value}")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
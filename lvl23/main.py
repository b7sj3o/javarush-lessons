import asyncio


class MyContextManager:
    def __enter__(self):
        print("До запуску")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Після запуску")
        if exc_type is not None:
            raise exc_type

# with MyContextManager():
#     print("Всередині менеджера")


# print("--------")


class AsyncContextManager:
    async def __aenter__(self):
        print("До запуску")

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("Після запуску")
        if exc_type is not None:
            raise exc_type


async def main():
    async with AsyncContextManager():
        print("Всередині менеджера")


# asyncio.run(main())

class AsyncTimer:
    """Асинхронний контекстний менеджер: заміряє час входу/виходу."""

    async def __aenter__(self):
        self.start = asyncio.get_running_loop().time()

        print("  [Timer] вхід у контекст")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        elapsed = asyncio.get_running_loop().time() - self.start
        print(f"  [Timer] вихід, минуло {elapsed:.2f} с")
        return False



async def demo_async_context_manager():
    print("--- Асинхронний контекстний менеджер ---")
    async with AsyncTimer():
        await asyncio.sleep(.7)
        print("  робота всередині контексту")
    print()

# asyncio.run(demo_async_context_manager())


import aiohttp
import asyncio


async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    html = await fetch_page('https://api.github.com/users/defunkt')
    print(html)

# asyncio.run(main())


import httpx


async def fetch_page(url):
    async with httpx.AsyncClient() as session:
        response = await session.get(url)
        return response.json()


async def main():
    html = await fetch_page('https://api.github.com/users/defunkt')
    print(html)

# asyncio.run(main())


class arange:
    """Асинхронний ітератор: аналог range з затримкою на кожен крок."""

    def __init__(self, start: int, stop: int):
        self.current = start
        self.stop = stop

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.current >= self.stop:
            raise StopAsyncIteration
        await asyncio.sleep(0.05)
        value = self.current
        self.current += 1
        return value


async def demo_async_iterator():
    print("--- Асинхронний ітератор (AsyncRange) ---")
    async for x in arange(10, 14):
        print(f"{x}")
    print()

asyncio.run(demo_async_iterator())
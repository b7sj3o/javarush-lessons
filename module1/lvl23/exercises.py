import asyncio
import aiohttp

headers = {
    "x-api-key": "reqres_7662e8dc70c646f086e220115c9670c8",
}

async def fetch_pages(base_url: str, total_pages: int):
    """
    Асинхронний генератор: по черзі віддає вміст сторінок 1, 2, ..., total_pages.
    Корисно для великих списків (users, posts) без завантаження всього разом.
    """
    timeout = aiohttp.ClientTimeout(total=10)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        for page in range(1, total_pages + 1):
            url = f"{base_url}?page={page}" if "?" not in base_url else f"{base_url}&page={page}"
            try:
                async with session.get(url=url, headers=headers) as resp:
                    if resp.status != 200:
                        yield {"page": page, "error": resp.status}
                        continue
                    data = await resp.json()
                    yield {"page": page, "data": data}
            except Exception as e:
                yield {"page": page, "error": str(e)}


async def demo_pagination():
    print("--- Практика: асинхронний генератор (пагінація) ---")
    # reqres.in підтримує реальну пагінацію: ?page=1,2,3
    base = "https://reqres.in/api/users"

    count = 0
    async for chunk in fetch_pages(base, 3):
        if "data" in chunk:
            items = chunk["data"].get("data", chunk["data"]) if isinstance(chunk["data"], dict) else chunk["data"]
            n = len(items) if isinstance(items, list) else 1
            count += n
            print(f"  Сторінка {chunk['page']}: отримано записів — {n}")
            print(chunk["data"])
        else:
            print(f"  Сторінка {chunk['page']}: помилка {chunk.get('error')}")
    print(f"  Всього записів: {count}\n")



class AsyncLineStream:
    """
    Асинхронний ітератор: імітує читання рядків з джерела з затримкою.
    Може представляти читання з сокета, файлу або API, що віддає stream.
    """

    def __init__(self, lines: list[str], delay: float = 0.1):
        self.lines = lines
        self.delay = delay
        self._index = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._index >= len(self.lines):
            raise StopAsyncIteration
        await asyncio.sleep(self.delay)
        line = self.lines[self._index]
        self._index += 1
        return line


async def demo_stream():
    print("--- Практика: асинхронний ітератор (стрім рядків) ---")
    stream = AsyncLineStream(["перший рядок", "другий", "третій"], delay=1)
    async for line in stream:
        print(f"отримано: {line!r}")
    print()


class AsyncRateLimiter:
    """Асинхронний контекстний менеджер: дозволяє виконання не частіше ніж раз на min_interval секунд."""

    def __init__(self, min_interval: float):
        self.min_interval = min_interval
        self._last_use = 0.0

    async def __aenter__(self):
        now = asyncio.get_running_loop().time()
        wait = self._last_use + self.min_interval - now
        if wait > 0:
            await asyncio.sleep(wait)
        self._last_use = asyncio.get_running_loop().time()
        return self

    async def __aexit__(self, *args):
        return False


async def demo_rate_limiter():
    print("--- Практика: контекстний менеджер (rate limiter) ---")
    limiter = AsyncRateLimiter(min_interval=1)
    for i in range(3):
        async with limiter:
            print(f"  виклик {i + 1} дозволено в {asyncio.get_running_loop().time():.2f}")
    print()


if __name__ == "__main__":
    asyncio.run(demo_rate_limiter())
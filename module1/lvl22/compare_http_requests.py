import asyncio
import aiohttp
import requests
import time
from aiohttp.client_exceptions import ClientConnectorDNSError
from concurrent.futures import ThreadPoolExecutor, as_completed


URLS = [
    "https://httpbin.org/get",
    "https://httpbin.org/ip",
    "https://api.github.com",
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://api.agify.io?name=Alex",
    "https://httpbin.org/uuid",
    "https://dog.ceo/api/breeds/image/random",
    "https://catfact.ninja/fact",
    "https://api.ipify.org?format=json",
    "https://httpbin.org/headers",
    "https://httpbin.org/json",
    "https://api.github.com/zen",
    "https://jsonplaceholder.typicode.com/users/1",
    "https://api.kanye.rest/",
    "https://randomuser.me/api/",
    "https://httpbin.org/delay/0",
    "https://api.zippopotam.us/us/90210",
    "https://reqres.in/api/users/1",
]


def fetch_sync(url):
    resp = requests.get(url)
    return resp.text


async def fetch_async(session: aiohttp.ClientSession, url: str):
    try:
         async with session.get(url) as response:
                return await response.text()
    except ClientConnectorDNSError:
        print(f"Невалідне посилання: {url}")


async def run_async():
    async with aiohttp.ClientSession() as session:
        start = time.perf_counter()

        tasks = (asyncio.create_task(fetch_async(session, url)) for url in URLS)
        results = await asyncio.gather(*tasks)

        elapsed = time.perf_counter() - start

        print(f"Всі запити зайняли: {elapsed:.3f}с (асинхронно)")

        # for result in results:
        #     print(result)

def run_sync():
    start = time.perf_counter()
    for url in URLS:
        fetch_sync(url)
    elapsed = time.perf_counter() - start

    print(f"Всі запити зайняли: {elapsed:.3f}с (синхронно)")


def run_multiprocessing():
    start = time.perf_counter()

    with ThreadPoolExecutor(max_workers=30) as executor:
        futures = [executor.submit(fetch_sync, url) for url in URLS]

    elapsed = time.perf_counter() - start

    print(f"Всі запити зайняли: {elapsed:.3f}с (multiprocessing)")

asyncio.run(run_async())
run_sync()
run_multiprocessing()
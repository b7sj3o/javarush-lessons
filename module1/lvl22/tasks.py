"""
Завдання 3: Система обробки логів (Producer-Consumer)
1 виробник (генерує лог кожну секунду) + 3 споживачі (пишуть у файл з затримкою).
"""

import asyncio
import random
import string

LOG_FILE = "logs.txt"
PRODUCE_SECONDS = 1000   # скільки секунд виробник генерує логи
CONSUMER_DELAY = 0.3  # імітація затримки запису (сек)


def random_log():
    """Генерує випадковий рядок-лог."""
    length = random.randint(10, 40)
    msg = "".join(random.choices(string.ascii_letters + string.digits, k=length))
    return f"[LOG] {msg}\n"


async def producer(queue: asyncio.Queue, duration_sec: int):
    """Корутина-виробник: кожну секунду кладе лог у чергу."""
    for _ in range(duration_sec):
        log_line = random_log()
        await queue.put(log_line)
        print(f"[Producer] sent: {log_line.strip()[:50]}...")
    # Сигнал завершення для кожного споживача
    for _ in range(3):
        await queue.put(None)


async def consumer(consumer_id: int, queue: asyncio.Queue):
    """Корутина-споживач: бере логи з черги, 'записує' у файл (з затримкою)."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        while True:
            item = await queue.get()
            if item is None:
                queue.task_done()
                break
            await asyncio.sleep(CONSUMER_DELAY)  # імітація затримки запису
            f.write(item)
            f.flush()
            print(f"  [Consumer {consumer_id}] wrote 1 line")
            queue.task_done()


async def main():
    open(LOG_FILE, "w", encoding="utf-8").close()  # очистити файл
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue, PRODUCE_SECONDS))
    consumers = [
        asyncio.create_task(consumer(1, queue)),
        asyncio.create_task(consumer(2, queue)),
        asyncio.create_task(consumer(3, queue)),
    ]

    await producer_task
    await asyncio.gather(*consumers)
    await queue.join()

    print(f"\nГотово. Логи записані в {LOG_FILE}")


if __name__ == "__main__":
    asyncio.run(main())

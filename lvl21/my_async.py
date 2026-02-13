import asyncio


async def task(name, delay):
    print(f"Початок: {name}")
    await asyncio.sleep(delay)
    print(f"Кінець {name}")


async def main():
    # results = await asyncio.gather(
    #     task("Task1", 1),
    #     task("Task2", 1.5),
    #     task("Task3", 0.5),
    # )

    loop = asyncio.get_event_loop()
    loop.run_until_complete(task("Task1", 1))
    loop.close()

    # task1 = asyncio.create_task(task("Task1", 1))

# asyncio.run(main())


async def background_job(name: str, duration: float) -> str:
    print(f"  [Фон] {name} стартував")
    await asyncio.sleep(duration)
    print(f"  [Фон] {name} завершився")
    return f"результат {name}"


async def example_create_task() -> None:
    print("\n--- Приклад 3: create_task — фонова задача ---")
    # Запускаємо задачу, але не чекаємо її одразу
    task = asyncio.create_task(background_job("Задача-A", 0.8))
    print("  Головна програма: задача запущена, роблю щось інше...")
    await asyncio.sleep(0.3)
    print("  Головна програма: тепер чекаю результат задачі")
    result = await task
    print(f"  Отримано: {result}\n")


# asyncio.run(example_create_task())


import asyncio

async def say(what, delay):
    await asyncio.sleep(delay)
    return what

async def main():
    task1 = asyncio.create_task(say('hello', 1))
    task2 = asyncio.create_task(say('world', 2))

    done, pending = await asyncio.wait([task1, task2], timeout=1.5)

    for task in done:
        print(task.result())

asyncio.run(main())
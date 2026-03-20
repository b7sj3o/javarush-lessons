import asyncio
loop = asyncio.get_event_loop()
new_loop = asyncio.new_event_loop()

asyncio.set_event_loop(new_loop)


# def send_notification(text):
#     print(f"Вам надійшло сповіщення: {text}")
#
# loop = asyncio.get_event_loop()
# when = loop.time() + 2
# loop.call_at(when, send_notification, "hello")
# loop.run_forever()

async def long_task():
    print("Старт задачі")
    await asyncio.sleep(5)
    print("Завдання завершене")


async def main():
    task = asyncio.create_task(long_task())  # Завдання створене
    print("Я можу робити інші речі поки завдання працює")

    await task  # Тут ми чекаємо, поки завдання закінчиться
    print("Тепер ми точно знаємо, що завдання завершилось")

# asyncio.run(main())


async def background_task():
    for i in range(5):
        await asyncio.sleep(1)
        print(f"Фонове завдання крок {i+1}")

async def main():
    task = asyncio.create_task(background_task())  # стартує одразу
    for i in range(3):
        print(f"Головна робота {i+1}")
        await asyncio.sleep(1)
    await task  # чекаємо завершення фонової задачі
    # run_until_complete
    print("Всі завдання завершились")


# asyncio.run(main())

import contextlib


async def long_running_task():
    print("Задача почалась...")
    await asyncio.sleep(10)
    print("Задача завершена...")

async def main():
    task = asyncio.create_task(long_running_task())

    await asyncio.sleep(1)
    task.cancel()


    with contextlib.suppress(asyncio.CancelledError):
        await task


# asyncio.run(main())


def callback(future):
    print("Task completed")

async def main():
    task = asyncio.create_task(asyncio.sleep(2))
    task.add_done_callback(callback)
    await task

asyncio.run(main())
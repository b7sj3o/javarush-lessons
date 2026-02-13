import threading
import time
#
#
# def worker(name: str, seconds: float) -> None:
#     """Функція, яка виконується в окремому потоці."""
#     print(f"  [{name}] почав роботу")
#     time.sleep(seconds)
#     print(f"  [{name}] закінчив роботу за {seconds} сек")
#
# start = time.time()
# threads = []
# for i in range(1, 11):
#     thread = threading.Thread(target=worker, args=(f"worker {i}", 3))
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()
#
# end = time.time()
#
# print(f"Код зайняв {end-start}с")
#
#
shared_counter = 0
counter_lock = threading.Lock()

def increment_counter(times: int) -> None:
    global shared_counter
    for _ in range(times):
        with counter_lock:  # тільки один потік одночасно може виконувати цей блок
            shared_counter += 1
            time.sleep(0.001)  # імітація роботи


def example_lock() -> None:
    global shared_counter
    shared_counter = 0
    print("\n--- Lock: захист спільного ресурсу (лічильник) ---")
    threads = [
        threading.Thread(target=increment_counter, args=(100,)),
        threading.Thread(target=increment_counter, args=(100,)),
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"  Підсумок: shared_counter = {shared_counter} (очікувано 200).\n")

# example_lock()


counter = 0

def increment_counter():
    global counter
    for _ in range(1000):
        tmp = counter
        counter = tmp + 1


# threads = []
# print("Starting threads")
# for _ in range(2):
#     thread = threading.Thread(target=increment_counter)
#     thread.start()
#     threads.append(thread)
#
# for thread in threads:
#     thread.join()


print(counter)


items = []
condition = threading.Condition()


def producer() -> None:
    time.sleep(1)  # імітація підготовки
    with condition:
        items.append("дані")
        print("  Виробник: додав дані, сповіщаю споживача")
        condition.notify()
    time.sleep(0.1)


def consumer() -> None:
    with condition:
        print("  Споживач: чекаю дані...")
        condition.wait()  # чекає, поки producer не викличе notify()
        print("  Споживач: отримав", items.pop())


def example_condition() -> None:
    print("\n--- Condition: виробник і споживач ---")
    t1 = threading.Thread(target=consumer)
    t2 = threading.Thread(target=producer)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Готово.\n")

example_condition()




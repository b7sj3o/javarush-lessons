tasks = []

def show_menu():
    print("1. Додати завдання")
    print("2. Показати завдання")
    print("3. Позначити виконаним")
    print("4. Видалити")
    print("5. Вийти")
    print()


def add_task():
    task = input("Введіть задачу: ").strip()

    if task == "":
        print("Введіть нормальну задачу!")
        return

    tasks.append({
        "title": task,
        "done": False
    })


def show_tasks():
    for count, task in enumerate(tasks, start=1):
        print(f"{count}. {"✅" if task["done"] else ""} {task['title']}")
    print()

def complete_task():
    show_tasks()

    user_number = int(input("Введіть номер завдання, яке потрібно позначити виконаним"))

    if 1 <= user_number <= len(tasks):
        tasks[user_number-1]["done"] = True


def delete_task():
    show_tasks()

    user_number = int(input("Введіть номер завдання, яке потрібно видалити"))

    if 1 <= user_number <= len(tasks):
        del tasks[user_number-1]


while True:
    show_menu()

    num = int(input("Введіть число: "))

    if num == 1:
        add_task()
    elif num == 2:
        show_tasks()
    elif num == 3:
        complete_task()
    elif num == 4:
        delete_task()
    else:
        break


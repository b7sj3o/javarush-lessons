# ===============================
# append() — додати в кінець
# ===============================

shopping_list = ["bread", "milk"]
shopping_list.append("eggs")
print("append:", shopping_list)


# ===============================
# extend() — додати багато елементів
# ===============================

shopping_list = ["bread", "milk"]
extra_items = ["eggs", "cheese"]
shopping_list.extend(extra_items)
print("extend:", shopping_list)


# ===============================
# insert() — вставити в конкретне місце
# ===============================

tasks = ["wash dishes", "do homework"]
tasks.insert(0, "call mom")
print("insert:", tasks)


# ===============================
# remove() — видалити конкретний елемент
# ===============================

shopping_list = ["bread", "milk", "eggs"]
shopping_list.remove("milk")
print("remove:", shopping_list)


# ===============================
# pop() — видалити і повернути елемент
# ===============================

tasks = ["task 1", "task 2", "task 3"]
done_task = tasks.pop()
print("pop (done):", done_task)
print("after pop:", tasks)


# ===============================
# clear() — очистити список
# ===============================

tasks = ["task 1", "task 2"]
tasks.clear()
print("clear:", tasks)


# ===============================
# index() — знайти індекс елемента
# ===============================

queue = ["Anna", "Bob", "Charlie"]
position = queue.index("Bob")
print("index:", position)


# ===============================
# count() — порахувати входження
# ===============================

grades = [5, 4, 5, 3, 5]
print("count:", grades.count(5))


# ===============================
# sort() — сортування списку
# ===============================

prices = [120, 50, 300, 80]
prices.sort()
print("sort:", prices)


# ===============================
# reverse() — перевернути список
# ===============================

messages = ["Hi", "How are you?", "Bye"]
messages.reverse()
print("reverse:", messages)


# ===============================
# МІНІ-ПРОГРАМА: ToDo список
# ===============================

tasks = []

# додаємо справи
tasks.append("Wake up")
tasks.append("Brush teeth")
tasks.extend(["Study Python", "Go for a walk"])

# вставляємо термінову справу
tasks.insert(0, "Check phone")

# виконуємо першу справу
done_task = tasks.pop(0)
print("Done:", done_task)

# видаляємо неактуальну справу
tasks.remove("Go for a walk")

# сортуємо справи
tasks.sort()

print("Tasks left:")
for task in tasks:
    print("-", task)
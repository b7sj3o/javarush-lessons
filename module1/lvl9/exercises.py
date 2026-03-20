
# 1
def analyze_inventory(data: list, min_quantity: int) -> tuple[int, list]:
    suma = 0
    goods_to_buy = []

    for name, quantity, price in data:
        suma += quantity * price
        if quantity < min_quantity:
            goods_to_buy.append(name)

    return suma, goods_to_buy

inventory = [
    ("Laptop", 10, 25000),
    ("Mouse", 50, 450),
    ("Keyboard", 32, 900),
    ("Monitor", 5, 6000),
    ("Headphones", 0, 1500),
]

# print(analyze_inventory(inventory, 10))
# print(analyze_inventory(inventory, 100))



# 2
import math

def calculate_path(points: list) -> float:
    total = 0

    for i in range(1, len(points)):
        x1,y1 = points[i-1]
        x2,y2 = points[i]

        total += math.sqrt((x2-x1)**2 + (y2-y1)**2)

    return total

route = [(0, 0), (3, 4), (6, 8), (6, 12)]
# print(calculate_path(route))


# 3

def get_top_student(students_list: list) -> tuple[str, float]:
    max_avg_grade = -1

    # Розраховуємо найбільший середній бал
    for name, grades in students_list:
        avg_grade = sum(grades) / len(grades)
        if avg_grade > max_avg_grade:
            max_avg_grade = avg_grade

    # Знаходимо всіх студентів з найбільшим балом
    students_with_max_grade = [
        name for name, grades in students_list
        if max_avg_grade == sum(grades) / len(grades)
    ]

    if len(students_with_max_grade) > 1:
        result_student = students_with_max_grade
    else:
        result_student = students_with_max_grade[0]

    return result_student, round(max_avg_grade,1)


students = [
    ("Alice", [85, 90, 92]),
    ("Bob", [70, 65, 80]),
    ("Charlie", [95, 100, 98]),
    ("Diana", [88, 85, 90]),
]

print(get_top_student(students))
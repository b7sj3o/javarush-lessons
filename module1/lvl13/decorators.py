# def debug(func):
#     def wrapper(*args, **kwargs):
#         print("Тут якийсь код до функції...")
#         func(*args, **kwargs)
#         print("Тут якийсь код після функції...")
#     return wrapper
#
# @debug
# def print_something(a,b,c):
#     print(f"Це наша функція, {a}, {b}, {c}")
#
#
# print_something(1,2,c=3)


# def repeat(num_times):
#     def decorator_repeat(func):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 func(*args, **kwargs)
#         return wrapper
#     return decorator_repeat
#
#
# @repeat(3)
# def say_hello(name):
#     print(f"Hello, {name}!")
#
# say_hello("me")


# def log_call(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__} args={args} kwargs={kwargs}")
#         result = func(*args, **kwargs)
#         print(f"Done {func.__name__} -> {result}")
#         return result
#     return wrapper
#
# @log_call
# def add(a, b):
#     return a + b
#
#
# add(2, 3)

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print("Start time:", start)
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"Function {func.__name__} took {elapsed:2f}s")
        return result
    return wrapper
#
# @timer
# def work():
#     sum = 0
#     for i in range(1, 100000000):
#         sum += i
#     return sum
#
#
# work()

# def simple_cache(func):
#     cache = {}
#     def wrapper(x):
#         if x in cache:
#             return cache[x]
#         cache[x] = func(x)
#         return cache[x]
#     return wrapper
#
# @simple_cache
# def fib(n):
#     time.sleep(0.1)
#     if n < 2:
#         return n
#     return fib(n - 1) + fib(n - 2)
#
# print(fib(10))
# print(fib(10))


# def require_admin(func):
#     def wrapper(user, *args, **kwargs):
#         if user.get("role") != "admin":
#             raise PermissionError("Admins only")
#         return func(user, *args, **kwargs)
#     return wrapper
#
# @require_admin
# def delete_user(user, user_id):
#     print(f"Deleted user {user_id}")
#
# delete_user({"name": "Ann", "role": "admin"}, 123)


# def retry(attempts, delay_seconds=0.0):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             last_exc = None
#             for i in range(attempts):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as exc:
#                     last_exc = exc
#                     print(f"Attempt {i + 1}/{attempts} failed: {exc}")
#                     if delay_seconds:
#                         time.sleep(delay_seconds)
#             raise last_exc
#         return wrapper
#     return decorator
#
# state = {"calls": 0}
#
# @retry(5, delay_seconds=0.1)
# def sometimes_fails():
#     state["calls"] += 1
#     if state["calls"] < 3:
#         raise ValueError("Not ready yet")
#     return "OK"
#
# print(sometimes_fails())
#
#
# from functools import wraps
#
# def debug(func):
#     @wraps(func)  # зберігає __name__/__doc__/__wrapped__ оригінальної функції
#     def wrapper(*args, **kwargs):
#         print(f"[debug] calling {func.__name__} args={args} kwargs={kwargs}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @debug
# def greet(name: str) -> str:
#     """Return greeting text."""  # цей докстрінг збережеться завдяки wraps
#     return f"Hi, {name}!"
#
# # print(greet.__name__)
# # print(greet.__doc__)
#
#
#
# # ЗАДАЧІ
#
# def validate_int(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if not isinstance(arg, int):
#                 return None
#         for k,v in kwargs.items():
#             if not isinstance(v, int):
#                 return None
#         return func(*args, **kwargs)
#     return wrapper

# def dec1(func):
#     def wrapper():
#         print("dec1 До")
#         func()
#         print("dec1 Після")
#     return wrapper
#
#
# def dec2(func):
#     def wrapper():
#         print("dec2 До")
#         func()
#         print("dec2 Після")
#     return wrapper
#
#
# @dec1
# @dec2
# def func():
#     print("Hello world")
#
#
# func()

# def enforce_types(func):
#     def wrapper(*args, **kwargs):
#         for idx, (k,v) in enumerate(func.__annotations__.items()):
#             # if not type(kwargs[k]) == v:
#             #     raise TypeError(f"{k} must be {v}")
#             if not type(args[idx]) == v:
#                 raise TypeError(f"{k} must be {v}")
#
#
#         return func(*args, **kwargs)
#     return wrapper
#
#
# @enforce_types
# def repeat(text: str, n: int):
#     return text * n
#
# repeat("Hi", 3)      # Ок
# repeat("Hi", "3")

def d1(func):
    def wrapper_d1():
        print("d1: перед")
        func()
        print("d1: після")
    return wrapper_d1

def d2(func):
    def wrapper_d2():
        print("d2: перед")
        func()
        print("d2: після")
    return wrapper_d2

@d1
@d2
def hello():
    print("hello")

hello()
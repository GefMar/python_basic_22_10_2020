import os
import sys

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""


# def log(func):
#     def wrapper(*args, **kwargs):
#         with open('some.log', 'a', encoding='UTF-8') as log_file:
#             log_file.write(f'{func.__name__} start with args : {args}, kwargs: {kwargs}')
#         result = func(*args, **kwargs)
#         return result
#
#     return wrapper

# @log
# def some_one(a, b):
#     return a + b


print(sys.argv)
print(__file__)
print(os.getenv('PWD'))
current_path = os.path.dirname(os.path.join(os.getenv('PWD'), __file__))
print(os.listdir(current_path))

# def my_decorator(func):
#     def wrapper():
#         print('Funtion will be decorated')
#         func()
#         print('Function is decorated now')
#     return wrapper
# def sayHello():
#     print('hello world')
    
# decoratedHello = my_decorator(sayHello)
# decoratedHello()
from functools import wraps
def my_decorator(func):
    def wrapper():
        print('Funtion will be decorated')
        func()
        print('Function is decorated now')
    return wrapper
@my_decorator
def sayHello():
    print('hello world')
    
sayHello()

def my_other_decorator(func):
    @wraps(func)
    def wrappper(*args,**kwargs):
        print(f"calling the function: {func.__name__}...")
        result = func(*args,**kwargs)
        print('Function called finished')
        return result
    return wrappper
        
    
@my_other_decorator
def calculate_sum(a,b):
    return a+b

print(calculate_sum(2,10))
print(calculate_sum.__name__)
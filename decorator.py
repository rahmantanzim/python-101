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
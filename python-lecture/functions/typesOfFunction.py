# decorater , generator , nested function,

def my_decorator(func):

    def wrapper():
        print("Before function")

       

        print("After function")

    return wrapper



def hello():
    print("Hello World")


hello()
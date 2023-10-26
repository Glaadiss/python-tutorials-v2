from functools import wraps


def with_uppercase(function):
    @wraps(function)
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def with_splitting(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


@with_uppercase
def say_hi():
    """This will say hi"""
    return "hello there"


print(say_hi.__name__, say_hi.__doc__)


@with_splitting
def say_hi():
    """This will say hi"""
    return "hello there"


print(say_hi.__name__, say_hi.__doc__)

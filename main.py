def concat(some_str):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result + some_str
        return wrapper
    return decorator


@concat("!")
def say_hi(name):
    return name


print(say_hi("Test"))
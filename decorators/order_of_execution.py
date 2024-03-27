
def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper


def bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<bold>{result}</bold>"
    return wrapper



# They are executed from bottom to top -
# first it makes the result from the function uppercase, then applies the bold tag
# <bold>HELLO</bold>

@bold
@upper
def base_func():
    """some docs"""
    return "Hello"


print(base_func())
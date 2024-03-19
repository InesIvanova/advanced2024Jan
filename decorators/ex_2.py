from functools import wraps


def vowel_filter(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return [el for el in result if el.lower() in 'aeyoui']
    return wrapper

@vowel_filter
def get_letters():
    """some docs here"""
    return ["a", "b", "c", "d", "e"]

print(get_letters())

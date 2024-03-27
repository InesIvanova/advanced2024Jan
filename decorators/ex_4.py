def multiply(a, *nums):
    def decorator(ref_func):
        def wrapper(*args, **kwargs):
            result = ref_func(*args, **kwargs)
            return [result*el for el in nums]
        return wrapper
    return decorator

@multiply(1, 2,3)
def sum_nums(num_1, num_2, ):
    return num_1 + num_2

print(sum_nums(1,num_2 =2))
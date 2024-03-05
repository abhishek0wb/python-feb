import time



def cache(func):
    cache_value ={}
    print(cache_value)
# instead of using list we are using dictary here because it solve the indexing problem.  
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache
def calcu(a,b):
    time.sleep(3)
    return a+b

print(calcu(4, 5))
print(calcu(6, 5))
print(calcu(4, 5))
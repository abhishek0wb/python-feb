import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time period")
        return result
    return wrapper

# decortors created

@timer
def extra(n):
    time.sleep(n)

extra(2)

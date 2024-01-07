import time

def time_logger(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} executed in {end_time - start_time} seconds.")
        return result
    return wrapper
  
@time_logger
def sample_function(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

# Calling the decorated function
print(sample_function(10000))

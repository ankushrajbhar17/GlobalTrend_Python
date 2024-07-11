import time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of '{func.__name__}': {execution_time:.4f} seconds")
        return result
    return wrapper

@measure_time
def computationally_expensive_function():
    total=100
    for i in range(10000000):
        pass
computationally_expensive_function()

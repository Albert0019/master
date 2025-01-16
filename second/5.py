import time
from functools import wraps

def time_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Function {func.__name__} took {elapsed_time:.6f} seconds to execute")
        return result
    return wrapper

# Test function 1
@time_decorator
def add_numbers(a: int, b: int):
    result = a + b
    print(f"Sum: {result}")
    return result

# Test function 2
@time_decorator
def calculate_from_file():
    with open('input.txt', 'r') as file:
        a, b = map(int, file.read().strip().split())
    result = a + b
    with open('output.txt', 'w') as file:
        file.write(str(result))

# Test
add_numbers(10, 20)  # Sum: 30
calculate_from_file()  # Assuming input.txt contains "10 20", writes "30" to output.txt
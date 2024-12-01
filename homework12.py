import time
from numpy import random


def time_decorator(func):
    
    def wrapper(*args, **kwargs):
        start_time = time.time() 
        result = func(*args, **kwargs)
        end_time = time.time()  
        print(f"Function `{func.__name__}` executed in {(end_time - start_time) * 10**3:.4f} ms.")
        return result
    return wrapper

n = 100
m = 20
lines = random.randint(100, size=(n, m))

file = open("MyFile.txt", "w")
for i in range(n):
    file.write(" ".join(map(str, lines[i])) + "\n")

def my_func(a):
    return a

file = open("MyFile.txt", "r")
lines = file.readlines()
processed_lines = []
for line in lines:
    numbers = map(int, line.split())
    filtered_numbers = filter(lambda x: x > 40, numbers)
    processed_lines.append(" ".join(map(str, filtered_numbers)) + "\n")

file = open("MyFile.txt", "w")
file.writelines(processed_lines)

def read_lines(filename):
    f = open(filename, "r")
    for line in f:
        yield line
    f.close()


@time_decorator
def print_file_lines(filename):
    for line in read_lines(filename):
        print(line)

print_file_lines("MyFile.txt")

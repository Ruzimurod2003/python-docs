# Функция как тип

def sum(a, b): return a + b
def multiply(a, b): return a * b
 
operation = sum
result = operation(5, 6)
print(result)   # 11
 
operation = multiply
print(operation(5, 6))      # 30

# Функция как параметр функции

def do_operation(a, b, operation):
    result = operation(a, b)
    print(f"result = {result}")
 
def sum(a, b): return a + b
def multiply(a, b): return a * b
 
do_operation(5, 4, sum)         # result = 9
do_operation(5, 4, multiply)   # result = 20

# Функция как результат функции

def sum(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
 
 
def select_operation(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply
 
 
operation = select_operation(1)     # operation = sum
print(operation(10, 6))             # 16
 
operation = select_operation(2)     # operation = subtract
print(operation(10, 6))             # 4
 
operation = select_operation(3)     # operation = multiply
print(operation(10, 6))             # 60
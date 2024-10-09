# Формальное определение лямбда-выражения
# lambda [параметры] : инструкция

square = lambda n: n * n
 
print(square(4))    # 16
print(square(5))    # 25

def select_operation(choice):
    if choice == 1:
        return lambda a, b: a + b
    elif choice == 2:
        return lambda a, b: a - b
    else:
        return lambda a, b: a * b
 
 
operation = select_operation(1)  # operation = sum
print(operation(10, 6))  # 16
 
operation = select_operation(2)  # operation = subtract
print(operation(10, 6))  # 4
 
operation = select_operation(3)  # operation = multiply
print(operation(10, 6))  # 60
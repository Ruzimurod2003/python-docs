'''
    while условное_выражение:
        инструкции
'''

number = 1
 
while number < 5:
    print(f"number = {number}")
    number += 1
print("Работа программы завершена")

number = 1
 
while number < 5:
    print(f"number = {number}")
    number += 1
else:
    print(f"number = {number}. Работа цикла завершена")
print("Работа программы завершена")

'''
    for переменная in набор_значений:
        инструкции
'''

message = "Hello"
 
for c in message:
    print(c)

for n in range(10):
    print(n, end=" ") # 0 1 2 3 4 5 6 7 8 9

for n in range(4, 10):
    print(n, end=" ") # 4 5 6 7 8 9

for n in range(0, 10, 2):
    print(n, end=" ") # 0 2 4 6 8

message = "Hello"
for c in message:
    print(c)
else:
    print(f"Последний символ: {c}. Цикл завершен");
print("Работа программы завершена")  # инструкция не имеет отступа, поэтому не относится к else

i = 1
j = 1
while i < 10:
    while j < 10:
        print(i * j, end="\t")
        j += 1
    print("\n")
    j = 1
    i += 1

number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, выходим из цикла
        break
    print(f"number = {number}")

number = 0
while number < 5:
    number += 1
    if number == 3 :    # если number = 3, переходим к новой итерации цикла
        continue
    print(f"number = {number}")
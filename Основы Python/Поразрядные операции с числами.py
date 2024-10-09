number = 5 # в двоичной форме 101
print(f"number = {number:0b}")  # number = 101

number = 0b101  # определяем число в двоичной форме
print(f"number = {number:0b}")  # number = 101
print(f"number = {number}")  # number = 5 - в десятичной системе

number1 = 1 # в двоичной системе 0b1
number2 = 2 # в двоичной системе 0b10
number3 = 3 # в двоичной системе 0b11
number4 = 4 # в двоичной системе 0b100
number5 = 5 # в двоичной системе 0b101
number6 = 6 # в двоичной системе 0b110

x1 = 2  # 010
y1 = 5  # 101
z1 = x1 & y1
print(f"z1 = {z1}")   # z1 = 0
 
x2 = 4  # 100
y2 = 5  # 101
z2 = x2 & y2
print(f"z2 = {z2}")   # z2 = 4
print(f"z2 = {z2:0b}")  # z2 = 100

x1 = 2      # 010
y1 = 5      # 101
z1 = x1|y1  # 111
 
print(f"z1 = {z1}")     # z1 = 7
print(f"z1 = {z1:0b}")  # z1 = 111
 
x2 = 4          # 100
y2 = 5          # 101
z2 = x2 | y2    # 101
print(f"z2 = {z2}")     # z2 = 5
print(f"z2 = {z2:0b}")  # z2 = 101

x = 9       #  1001
y = 5       #  0101
z = x ^ y   #  1100
print(f"z = {z}")       # z = 12
print(f"z = {z:0b}")   # z = 1100

x = 45       # Значение, которое надо зашифровать - в двоичной форме 101101
key = 102    # Пусть это будет ключ - в двоичной форме 1100110
 
encrypt = x ^ key    # Результатом будет число 1001011 или 75
print(f"Зашифрованное число: {encrypt}")
 
decrypt = encrypt ^ key    # Результатом будет исходное число 45
print(f"Расшифрованное число: {decrypt}")

x = 5
y = ~x
print(f"y: {y}")  # -6

a = 16 # в двоичной форме 10000
b = 2 
c = a << b  # Сдвиг числа 10000 влево на 2 разряда, равно 1000000 или 64 в десятичной системе
print(c)   #64
 
d = a >> b  #Сдвиг числа  10000  вправо на 2 разряда, равно 100 или 4 в десятичной системе
print(d)   #4

a = 22 # в двоичной форме 10110
b = 2
c = a << b  # Сдвиг числа 10110 влево на 2 разряда, равно 1011000 или 88 в десятичной системе
print(c)   # 88
 
d = a >> b  # Сдвиг числа 10110 вправо на 2 разряда, равно 101 или 5 в десятичной системе
print(d)   # 5
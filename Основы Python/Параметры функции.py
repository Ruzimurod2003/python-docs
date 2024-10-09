# def say_hello(name):
#     print(f"Hello, {name}")
 
# say_hello("Tom")
# say_hello("Bob")
# say_hello("Alice")

# Значения по умолчанию
# def say_hello(name="Tom"):
#     print(f"Hello, {name}")
 
 
# say_hello()         # здесь параметр name будет иметь значение "Tom"
# say_hello("Bob")    # здесь name = "Bob"

# Передача значений параметрам по имени. Именованные параметры
# def print_person(name, age):
#     print(f"Name: {name}  Age: {age}")
 
 
# print_person(age = 22, name = "Tom")

# Все параметры, которые располагаются справа от символа *, получают значения только по имени:
# def print_person(name, *,  age, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
 
 
# print_person("Bob", age = 41, company ="Microsoft")    # Name: Bob  Age: 41  company: Microsoft

# Все параметры, которые идут до символа / , являются позиционными и могут получать значения только по позиции
# def print_person(name, /, age, company="Microsoft"):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
 
 
# print_person("Tom", company="JetBrains", age = 24)     # Name: Tom  Age: 24  company: JetBrains
# print_person("Bob", 41)                 # Name: Bob  Age: 41  company: Microsoft

# Для одной функции можно определять одновременно позиционные и именнованные параметры.

# def print_person(name, /,  age = 18, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
 
 
# print_person("Sam", company ="Google")               # Name: Sam  Age: 18  company: Google
# print_person("Tom", 37, company ="JetBrains")        # Name: Tom  Age: 37  company: JetBrains
# print_person("Bob", company ="Microsoft", age = 42)  # Name: Bob  Age: 42  company: Microsoft

# Неопределенное количество параметров
# def sum(*numbers):
#     result = 0
#     for n in numbers:
#         result += n
#     print(f"sum = {result}")
 
 
# sum(1, 2, 3, 4, 5)      # sum = 15
# sum(3, 4, 5, 6)         # sum = 18


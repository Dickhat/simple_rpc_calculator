from xmlrpc.server import SimpleXMLRPCServer
from math import sqrt

# Функция для сложения двух чисел
def sum_numbers(a, b):
    return a + b

# Функция для вычитания двух чисел
def sub_numbers(a, b):
    return a - b

# Функция для умножения двух чисел
def mul_numbers(a, b):
    return a*b

# Функция для деления двух чисел
def div_numbers(a, b):
    if(b == 0):
        return "Деление невозможно"
    else:
        return a/b

# Функция для получения квадратного корня
def sqrt_number(a):
    if(a <= 0):
        return "Операция взятия корня невозможна"
    else:
        return sqrt(a)

# Функция для получения процентов от числа
def percent_number(a, b):
    if(b < 0):
        return "Проценты не могут быть отрицательными"
    else:
        return (a*b)/100

# Функция для получения округленного числа
def round_number(a, b):
    return round(a, b)

# Функция для получения степени числа
def pow_number(a, b):
    return a**b

# Функция для выполнения последовательности операций
def sequence_operations(operations):
    result = None

    for number in range(len(operations)):
        # Извлекаем название операции и её параметры
        temp = operations[number]
        operation_name, params = temp.popitem()

        a = params.get("a")
        b = params.get("b") 

        # Используем результат предыдущей операции, если указан "result"
        if a == "result":
            a = result

        if (operation_name == 'add'):
            result = sum_numbers(a, b)
        elif(operation_name == 'sub'):
            result = sub_numbers(a, b)
        elif(operation_name == 'mul'):
            result = mul_numbers(a, b)
        elif(operation_name == 'div'):
            result = div_numbers(a, b)
        elif(operation_name == 'sqrt'):
            result = sqrt_number(a)
        elif(operation_name == 'percent'):
            result = percent_number(a, b)
        elif(operation_name == 'rnd'):
            result = round_number(a, b)
        elif(operation_name == 'pw'):
            result = pow_number(a, b)
    
    return result

# Создаем сервер на порту 9000
server = SimpleXMLRPCServer(("localhost", 9000))
print("RPC-сервер запущен на порту 9000...")

# Регистрируем функцию для суммирования
server.register_function(sum_numbers, "sum")

# Регистрируем функцию для вычитания
server.register_function(sub_numbers, "sub")

# Регистрируем функцию для умножения
server.register_function(mul_numbers, "mul")

# Регистрируем функцию для деления
server.register_function(div_numbers, "div")

# Регистрируем функцию для квадратного корня
server.register_function(sqrt_number, "sqrt")

# Регистрируем функцию для получения процентов от числа
server.register_function(percent_number, "percent")

# Регистрируем функцию для получения округленного числа
server.register_function(round_number, "rnd")

# Регистрируем функцию для получения степени числа
server.register_function(pow_number, "pw")

# Регистрируем функцию для последовательности операций
server.register_function(sequence_operations, "seq")

# Запускаем сервер
server.serve_forever()

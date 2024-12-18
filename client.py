import xmlrpc.client

# Подключаемся к серверу
server = xmlrpc.client.ServerProxy("http://localhost:9000/")

method_name = ''

while method_name == '':
    print("\nДоступные операции:\n1)Суммирование;\n2)Вычитание;\n3)Умножение;\n4)Деление;\n5)Извлечение квадратного корня;")
    print("6)Получение процентов от числа\n7)Округление числа;\n8)Возвести в степень;\n9)Последовательность операций;\n")
    chosen_method = int(input("Введите номер операции:"))

    if(chosen_method == 1):
        method_name = "Суммирование"

        # Вызываем метод для сложения двух чисел
        number1 = float(input("Введите первое число a:"))
        number2 = float(input("Введите второе число b:"))
        result = server.sum(number1, number2)

        # Вывод результата
        print(f"Результат сложения {number1} + {number2} = {result}")
    elif (chosen_method == 2):
        method_name = "Вычитание"
        
        # Вызываем метод для вычитания двух чисел
        number1 = float(input("Введите первое число a:"))
        number2 = float(input("Введите второе число b:"))
        result = server.sub(number1, number2)
        
        # Вывод результата
        print(f"Результат вычитания {number1} - {number2} = {result}")
    elif (chosen_method == 3):
        method_name = "Умножение"
        
        # Вызываем метод для вычитания двух чисел
        number1 = float(input("Введите первое число a:"))
        number2 = float(input("Введите второе число b:"))
        result = server.mul(number1, number2)
        
        # Вывод результата
        print(f"Результат умножения {number1} * {number2} = {result}")
    elif (chosen_method == 4):
        method_name = "Деление"
        
        # Вызываем метод для вычитания двух чисел
        number1 = float(input("Введите первое число a:"))
        number2 = float(input("Введите второе число b:"))
        result = server.div(number1, number2)
        
        # Вывод результата
        print(f"Результат деления {number1} / {number2} = {result}")
    elif (chosen_method == 5):
        method_name = "Извлечение квадратного корня"
        
        # Вызываем метод для вычитания двух чисел
        number1 = float(input("Введите число a:"))
        result = server.sqrt(number1)
        
        # Вывод результата
        print(f"Результат вычисления квадратного корня от {number1} = {result}")
    elif (chosen_method == 6):
        method_name = "Получение процентов от числа"
        
        # Вызываем метод для получения процентов от числа
        number1 = float(input("Введите число a:"))
        number2 = float(input("Введите проценты от числа a:"))
        result = server.percent(number1, number2)
        
        # Вывод результата
        print(f"Результат вычисления {number2} процентов от числа {number1} = {result}")
    elif (chosen_method == 7):
        method_name = "Получение округленного числа"
        
        # Вызываем метод для получения процентов от числа
        number1 = float(input("Введите число a:"))
        number2 = int(input("Введите число знаков после запятой для округления:"))
        result = server.rnd(number1, number2)
        
        # Вывод результата
        print(f"Результат округления числа {number1} для {number2} знаков = {result}")
    elif (chosen_method == 8):
        method_name = "Получение степени числа"
        
        # Вызываем метод для получения процентов от числа
        number1 = float(input("Введите число a:"))
        number2 = float(input("Введите степень, в которую необходимо возвести число:"))
        result = server.pw(number1, number2)
        
        # Вывод результата
        print(f"Результат возведения числа {number1} в степень {number2} = {result}")
    elif (chosen_method == 9):
        method_name == "Последовательность операций"
        chosen_method = -1

        operations = []

        first_operation = True

        # Пока вводится последовательность операций
        while chosen_method != 9:
            print("\nДоступные операции:\n1)Суммирование;\n2)Вычитание;\n3)Умножение;\n4)Деление;\n5)Извлечение квадратного корня;")
            print("6)Получение процентов от числа\n7)Округление числа;\n8)Возвести в степень;\n9)Закончить ввод операций;\n")
            chosen_method = int(input("Введите номер операции:"))

            if (chosen_method == 1):
                if (first_operation == True):
                    number1 = float(input("Введите число a:"))
                    first_operation = False
                else:
                    number1 = "result"

                number2 = float(input("Введите число b:"))
                operations.append({'add':{'a':number1,'b':number2}})
            elif(chosen_method == 2):
                if (first_operation == True):
                    number1 = float(input("Введите число a:"))
                    first_operation = False
                else:
                    number1 = "result"

                number2 = float(input("Введите число b:"))
                operations.append({'sub':{'a':number1,'b':number2}})
            elif(chosen_method == 3):
                if (first_operation == True):
                    number1 = float(input("Введите число a:"))
                    first_operation = False
                else:
                    number1 = "result"
                
                number2 = float(input("Введите число b:"))
                operations.append({'mul':{'a':number1,'b':number2}})
            elif(chosen_method == 4):
                if (first_operation == True):
                    number1 = float(input("Введите число a:"))
                    first_operation = False
                else:
                    number1 = "result"
                
                number2 = float(input("Введите число b:"))
                operations.append({'div':{'a':number1,'b':number2}})
            elif(chosen_method == 5):
                if (first_operation == True):
                    number1 = float(input("Введите число a:"))            
                    first_operation = False
                else:
                    number1 = "result"
                    
                number2 = 0
                operations.append({'sqrt':{'a':number1,'b':number2}})
            elif(chosen_method == 6):
                if (first_operation == True):
                    number1 = float(input("Введите число a:"))            
                    first_operation = False
                else:
                    number1 = "result"
                    
                number2 = float(input("Введите число процентов от числа:"))
                operations.append({'percent':{'a':number1,'b':number2}})
            elif(chosen_method == 7):
                if (first_operation == True):
                    number1 = float(input("Введите число a:"))            
                    first_operation = False
                else:
                    number1 = "result"
                    
                number2 = int(input("Введите число знаков после запятой:"))
                operations.append({'rnd':{'a':number1,'b':number2}})
            elif(chosen_method == 8):
                if (first_operation == True):
                    number1 = float(input("Введите число a:"))
                    first_operation = False
                else:
                    number1 = "result"
                    
                number2 = float(input("Введите число b:"))
                operations.append({'pw':{'a':number1,'b':number2}})
        
        result = server.seq(operations)
        # Вывод результата
        print(f"Результат выполнения последовательности операций = {result}")
        exit()
    else:
        print("\n Введен некорректный номер операции")

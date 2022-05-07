print("Привет я калькулятор(вер4.0), Я ПРАКТИЧЕСКИ ВСЕМОГУЩ!!!!!!")
operation = input("Выберите операцию(+, +++, - , * , /): ")
zero = 0
if operation == "+":
    while True:
        try:
            number_1 = float(input("Введи первое число: "))
            number_2 = float(input("Введи второе число: "))
            print(number_1 + number_2)
            quit()
        except ValueError as err:
            print('Это не число!!!')
elif operation == "-":
    while True:
        try:
            number_1 = float(input("Введи первое число: "))
            number_2 = float(input("Введи второе число: "))
            print(number_1 - number_2)
            quit()
        except ValueError as err:
            print('Это не число!!!')
elif operation ==  "*":
    while True:
        try:
            number_1 = float(input("Введи первое число: "))
            number_2 = float(input("Введи второе число: "))
            print(number_1 * number_2)
            quit()
        except ValueError as err:
            print('Это не число!!!')
elif operation == "/":
    while True:
        try:
            number_1 = float(input("Введи первое число: "))
            number_2 = float(input("Введи второе число: "))
            print(number_1 / number_2)
            quit()
        except ValueError as err:
            print('Это не число!!!')
        except ZeroDivisionError as error:
            print('Бесконечность не предел!♾',error)
            quit()
elif operation == '+++':
      total = 0
      while True:
            number = input('Введите числа которые хотели бы сложить: ')
            try:
                total += float(number)
            except ValueError as err:
                   print('Это не число!!!')
            if number == '':
                try:
                    total += float(number)
                except ValueError as err:
                   print(f'результат: {total}')
                   quit()

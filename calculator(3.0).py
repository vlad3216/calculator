print("Привет я калькулятор(вер3.0), у меня тут новая функция появилась, называется множественное сложение, давай пробовать?")
operation = input("Выберите операцию(+, +++, - , * , /): ")
zero = 0
if operation == "+":
      number_1 = int(input("Введи первое целое число: "))
      number_2 = int(input("Введи второе целое число: "))
      print(number_1 + number_2)
elif operation == "-":
      number_1 = int(input("Введи первое целое число: "))
      number_2 = int(input("Введи второе целое число: "))
      print(number_1 - number_2)
elif operation ==  "*":
      number_1 = int(input("Введи первое целое число: "))
      number_2 = int(input("Введи второе целое число: "))
      print(number_1 * number_2)
elif operation == "/":
      number_1 = int(input("Введи первое целое число: "))
      number_2 = int(input("Введи второе целое число: ")) 
      try:
          zero /= number_2
      except ZeroDivisionError as error:
            print('Бесконечность не предел!♾',error)
            quit()
      print(number_1 / number_2)
elif operation == '+++':  
      total = 0
      while True:
            number = input('Введите числа которые хотели бы сложить: ')
            try:
                total += int(number)
            except ValueError as err:
                        print(total)
                        break
            


   
      

    
      

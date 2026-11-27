try:
    a = float(input("Введіть A: "))
    b = float(input("Введіть B: "))
    operation = input("Введіть операцію: ")
    if operation == "+":
        print(a + b)
    elif operation == "-":
        print(a - b)
    elif operation == "*":
        print(a * b)
    elif operation == "/":
         try:
            print("Результат:", a / b)
         except ZeroDivisionError:
            print("Помилка: на нуль ділити не можна.")
    else:
        print("Помилка: невідома операція.")
except ValueError:
    print("Помилка: потрібно ввести число." )
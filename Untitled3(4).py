students = ["Соловко", "Петриченко", "Коваленко", "Шевченко"]
grades = {
    "Математика": 11,
    "Історія": 10,
    "Українська": 12,
    "Англійська": 9
}
print("1-учень за індексом")
print("2-оцінка за назвою предмета")
try:
    choice = int(input("Оберіть тип пошуку: "))
    if choice == 1:
        try:
            index = int(input("Введіть індекс: "))
            print("Учень:", students[index])
        except ValueError:
            print("Помилка: індекс має бути цілим числом.")
        except IndexError:
            print("Помилка: учня з таким індексом немає.")
    elif choice == 2:
        subject = input("Введіть назву предмета: ")
        try:
            print("Оцінка:", grades[subject])
        except KeyError:
            print("Помилка: такого предмета немає.")
    else:
        print("Помилка: невідомий пункт меню.")
except ValueError:
    print("Помилка: потрібно ввести число 1 або 2.")
    
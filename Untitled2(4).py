def input_grade():
    while True:
        try:
            grade = int(input("Оцінка: "))
        except ValueError:
            print("Помилка: потрібно ввести ціле число.")
            continue
        try:
            if grade < 1 or grade > 12:
                raise ValueError("оцінка повинна бути від 1 до 12.")
            return grade
        except ValueError as error:
            print("Помилка:", error)
grade = input_grade()
print("Прийнято:", grade)

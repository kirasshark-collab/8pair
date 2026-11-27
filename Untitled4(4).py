good = []
skipped = 0
try:
    with open("students.txt", "r", encoding="utf-8") as file:
        for number, line in enumerate(file, start=1):
            parts = line.strip().split(";")
            reason = ""
            if len(parts) != 2:
                reason = "неправильна структура рядка"
            else:
                name = parts[0].strip()
                score_text = parts[1].strip()
                if name == "" or score_text == "":
                    reason = "неправильна структура рядка"
                else:
                    try:
                        score = int(score_text)
                    except ValueError:
                        reason = "бал не є цілим числом"
                    else:
                        if score < 0 or score > 100:
                            reason = "бал поза діапазоном"
            if reason != "":
                print(f"Рядок {number} пропущено: {reason}")
                skipped += 1
            else:
                good.append((name, score))
except FileNotFoundError:
    print("Помилка: файл students.txt не знайдено.")
else:
    good.sort(key=lambda x: x[1], reverse=True)
    with open("report.txt", "w", encoding="utf-8") as report:
        for name, score in good:
            report.write(f"{name};{score}\n")
    print("Правильних записів:", len(good))
    print("Пропущено:", skipped)
    print("Створено report.txt")
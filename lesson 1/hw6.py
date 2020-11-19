day = 1
a = int(input("Километраж в первый день: "))
b = int(input("Километраж в последний день: "))

while True:
    if a <= 0 or b < 0:
        print("Нужно было ввести положительное число!")
        break
    else:
        while a <= b:
            a += 0.1 * a
            day += 1
        print(f"{day}-й день: {a:.2f} км")
        print(f"на {day}-й день спортсмен достиг результата - не менее {b} км")
        break

def numbers():
    n = 0
    while True:
        num = input("введите числовые значения через пробел, далее нажмите Enter для вывода суммы чисел, для остановкии программы - нажмите q! ").split()
        for i in num:
            if i == "q":
                return n
            else:
                n += int(i)
            print(f"сумма введеных чисел = {n}")

print(numbers())


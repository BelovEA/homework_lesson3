"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их
деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на
ноль
"""
def numbers(num1, num2):
    num1, num2 = int(num1), int(num2)
    if num2 != 0:
        return num1 / num2
    else:
        print("введите любое число отличное от нуля при вводе второго числа!")

print(numbers(input("Введите первое число: "), input("введите второе число: ")))

print("_" * 20)
#Вариант с try/except
def numbers(num1, num2):
    try:
        num1, num2 = int(num1), int(num2)
        return num1 / num2
    except ZeroDivisionError:
        print("Err")
print(numbers(input("Введите первое число: "), input("введите второе число: ")))

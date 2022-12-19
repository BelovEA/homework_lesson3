"3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов."
def my_func():
    try:
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
        num3 = int(input('Введите третье число: '))
    except ValueError:
        return "Введите числа!"
    if num1 < num2 and num1 < num3:
            numbers = num2 + num3
    elif num2 < num3 and num2 < num1:
            numbers = num3 + num1
    elif num3 < num2 and  num3 < num1:
            numbers = num2 + num3
    return numbers
print(my_func())


print("-" * 50)

def my_func(num1, num2, num3):
    try:
        numbers = list(map(float, [num1, num2, num3]))
        return sum(sorted(numbers[1:]))
    except ValueError:
        return "Введите числа!"
print(my_func(input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: ')))

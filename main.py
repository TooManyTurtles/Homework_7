# Важливо: не використовувати цикли для реалізації основної логіки.
# Потрібно використати рекурсію.
# Цикл можна використовувати лише у 4 завданні для знаходження суми чисел.
# Завдання 1.
# Написати рекурсивну функцію знаходження ступеня числа.
# Завдання 2.
# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)
# Завдання 3.
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.
# Додатково:
# Завдання 4.
# Напишіть рекурсивну функцію, яка приймає одновимірний масив із 100 цілих чисел
# заповнених випадковим чином і знаходить позицію,
# з якої починається послідовність із 10 чисел, сума яких мінімальна.


# 1 Написати рекурсивну функцію знаходження ступеня числа.

def expo(number: int, power: int) -> int:
    if power == 0:
        return 1
    else:
        return number * expo(number, power - 1)

# Написати рекурсивну функцію, яка виводить N зірок у ряд, число N задає користувач.
# Проілюструйте роботу функції прикладом. (Протестувати)

def stars(number):
    if number != 0:
        print("*", end="")
        return stars(number - 1)


# Завдання 3.
# Написати рекурсивну функцію, яка обчислює суму всіх чисел у діапазоні від a до b.
# Користувач вводить a та b. Проілюструйте роботу функції прикладом.

def middle_sum(number1, number2, x=0):
    if number1 > number2:
        return x
    return middle_sum(number1 + 1, number2, x + number1)


try:

    number, power = map(int, input("Pls input number and power: ").split())
    stars_number = int(input("Pls input number of stars: "))
    number1, number2 = map(int, input("Pls input numbers, summ between, you want to find: ").split())

    print(f"Task one number is: {expo(number, power)}")
    print("Stars incoming", end= " ")
    stars(stars_number)
    print()
    print(middle_sum(number1, number2))

except Exception as e:
    print(e)

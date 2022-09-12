# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 6782 -> 23
# 0,56 -> 11

def input_number(input_text):
    while True:
        number = input(f"{input_text}")
        try:
            val = float(number)
            break
        except ValueError:
            print("Это не число!")     
        # else all is good, val is >=  0 and an integer
    return val

def digit_sum(n):
    sum = 0
    for i in str(n): 
        if i != ".":
            sum += int(i)
    return sum
   
n = input_number("Укажите число: ")
print(digit_sum(n))


# Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def input_number(input_text):
    while True:
        number = input(f"{input_text}")
        try:
            val = int(number)
            break
        except ValueError:
            print("Это не целое число!")     
        # else all is good
    return val

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)
n = input_number("Укажите число: ")
list = [factorial(i) for i in range(1, n + 1)] #list comprehension
print(list)


# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму, округлённую до трёх знаков после точки.
# Для n = 6 -> 14.072

def input_number(input_text):
    while True:
        number = input(f"{input_text}")
        try:
            val = int(number)
            break
        except ValueError:
            print("Это не целое число!")     
        # else all is good
    return val

def sum_seq(n):
    sum = 0
    for i in range(1, n + 1):
        sum += round((1 + 1 / i) ** i, 3)
    return sum
n = input_number("Укажите число: ")
print(sum_seq(n))


# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

def input_number(input_text):
    while True:
        n = input('Введите n: ')
        a = input('Введите a: ')
        b = input('Введите b: ')
        try:
            val_n = int(n)
            val_a = int(a)
            val_b = int(b)
            if val_a > val_n * 2 + 1 or val_b > val_n * 2 + 1:
                print("Введеное позиция вне диапазона, попробуйте снова!")
                continue
            break
        except ValueError:
            print("Это не целое число!")     
        # else all is good
    return val_n, val_a, val_b

def fill_list(n):
    list = [i for i in range(-n, n + 1)]
    return list

def print_list(n):
    list = [i for i in range(-n, n + 1)]
    print(list)
    
def multiply_elements(list, a, b):
    while a - 1 < len(list) and b - 1 < len(list):
        return list[a - 1] * list[b - 1]

n, a, b = input_number('')
list = fill_list(n)
print_list(n)
print(f'Произведение элементов на позициях {a} и {b} равно {multiply_elements(list, a, b)}')



# Задание 5 Реализуйте алгоритм перемешивания списка.
import random

list = [11, 22, 33, 44, 55, 66]
print("Начальный список: ", list)
n = len(list)
 
for i in range(n):
    j = random.randint(0, n - 1)
    element = list.pop(j)
    list.append(element)
print("Перемешанный список: ", list)
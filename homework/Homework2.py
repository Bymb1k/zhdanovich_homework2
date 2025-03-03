# Zhdanovich Valery
# Date: 03/03/2025
# Description: Homework 2
# Grodno IT Academy Python 3.9.6

# Чтобы запустить тесты и проверить выполнение домашнего задания:
# python test_Homework2.py

# Объяснение работы с функциями:
# формат определения функции (то есть: мы ее создаем) - def func(arg1, arg2, arg3)
# arg1, arg2, arg3 - это аргументы, которые передаются в функцию при ее вызове (то есть, мы ее запускаем)

# оценивается: чистота кода, наличие комментариев (PEP8), прохождение всех тестов
# нельзя менять названия функций/файлов/входные данные. Можно менять решение, менять/добавлять return.

# пример названия репозитория для гитхаба: kazukevich_homework2
# добавьте в репозиторий с домашним задание файл readme.md с датой сдачи, фамилией и именем выполнившего и кратким
# описанием каждой задачи (коротко, что использовали, алгоритм функции), оформленным в стиле markdown
# В репозитории не должно быть лишних папок и файлов: файлов IDE, виртуального окружения и тд
# ДЗ не коммититься в ветку main(master)! 

# Вы создаете репозиторий с ДЗ приватным. Чтобы добавить меня к репозиторию: нужно в настройках репозитория добавить collaborator:
# И ввести мой логин в github: karturik


# Напишите программу, ĸоторая считает общую цену.
# Передается m рублей и n ĸопееĸ цена, а таĸже ĸоличество s товара.
# Посчитайте общую цену в рублях и ĸопейĸах за l товаров.
# Уточнение:
# Используйте функцию return чтобы ответ был в рублях и копейках.
# Ответ должен быть в формате: "Общая цена составляет M рублей и N копеек за L товаров"

# * Для одного из тестов нужно применять какую-то библиотеку =)
from decimal import Decimal, getcontext
def common_price(m, n, s, l):
# Проверяем типы входных параметров
    if not isinstance(m, (int, float)) or not isinstance(n, (int, float)) or not isinstance(s, (int, float)) or not isinstance(l, (int, float)):
        return False
# Проверяем, чтобы s не равно 0  или l не отрицательное число  
    if s <= 0 or l < 0:
        return False
# Проверяем, чтобы m и n были не равны нулю    
    if m <= 0 and n <= 0:
        return False
# Устанавливаем точность для Decimal и увеличиваем точность
    getcontext().prec = 30  
# Используем Decimal для точных вычислений
    m = Decimal(m)
    n = Decimal(n)
    s = Decimal(s)
    l = Decimal(l)
# Умножаем m(рубли) на 100, то есть переводим их в копейки. Затем добавляем n(копейки). Затем мы делим общую цену на количество товаров s, чтобы узнать цену за один товар. И умножаем на количество товаров l.
    b = (m * 100 + n) / s * l
# Округляем до целого
    b = round(b)
# Делим b без остатка чтобы узнать рубли.
    a = b // 100
# Чтобы узнать копейки получаем остаток от b.
    v = b % 100
# Приравниваем аргумент l к строке d.
    d = l
    return "Общая цена составляет " + str(a) + " рублей и " + str(v) + " копеек за " + str(d) + " товаров"
price = common_price (10, 4, 7, 3)
print(price)



# В функцию передаются аргументы: a, b, c - длины сторон треугольника.
# Требуется: проверить, может ли существовать треугольник с такими длинами сторон.
# Если может - найти его площадь с точностью до четырёх десятичных и вернуть площадь (return).
# Пример: если строны треугольника равны 2, 2, 2 то мы должны вернуть 1.7321
# Если такой треугольник существовать не может - функция должна вернуть False.
def triangle(a, b, c):
# Проверяем все ли стороны треугольника положительные. Если хотя бы одна сторона отрицательная, то треугольник не существует.
  if not all(isinstance(x, (int, float)) for x in (a, b, c)):
    return False
# Проверяем правило треугольника: сумма длин любых двух сторон должна быть больше длины третьей стороны. Если правило не выполняется, то треугольник не существует.
  if not (a > 0 and b > 0 and c > 0):
    return False
# Вычисляем полупериметр треугольника.
  p = (a + b + c) / 2
# Импортируем модуль math для работы с числами.
  import math
# Вычисление площади по формуле Герона.
  S = math.sqrt(p * (p - a) * (p - b) * (p - c))
# Возвращаем округленную площадь до четырех десятичных знаков.
  return round(S, 4)
print(triangle(3, 3, 3))


# Найти самое длинное слово в введенном предложении.
# Учтите что в предложении могут быть знаки препинания.
# Пример: если передано "This is a sample sentence where the longest word is in the middle!",
# то надо вернуть "sentence"
def longest_word(sentence):
# Импортируем модуль для работы с текстом.
  import string
# Проверяем на пустое предложение.
  if not isinstance(sentence, str):
    return False
# Удаляем знаки препинания и разделяем предложение на слова. Используем регулярное выражение для поиска слов.
  translator = str.maketrans('', '', string.punctuation)
  cleaned_sentence = sentence.translate(translator)
# Разбиваем строку на слова
  words = cleaned_sentence.split()
# Проверяем, есть ли слова после разделения
  if not words: 
     return False
# Присваиваем переменной long_word пустую строку для хранения самого длинного слова в списке.
  long_word = ""
# Проверяем каждое слово из списка 
  for word in words:
# Проверяем длинну слова
    if len(word) > len(long_word):
# Если текущее слово длиннее, обновляем long_word
     long_word = word
# Если длины равны, сравниваем слова лексикографически
    elif len(word) == len(long_word):
     if word > long_word:
        long_word = word
     elif word < long_word:
        long_word = word

  return long_word
sentence = "This is a sample sentence where the longest word is in the middle!"
long_word = longest_word(sentence)
print(long_word)


# Передается строка. Требуется удалить из нее повторяющиеся символы и все пробелы.
# Например, если было передано "abc cde def", то должно быть выведено "abcdef".
def uniques(repeating_string):
    if not isinstance(repeating_string, str):
        return False
# Удаляем пробелы.
    repeating_string = repeating_string.replace(" ", "")
# Удаляем повторяющиеся символы, сохраняя порядок.
    result = ""
# Проверяем каждый символ в строке и добавляем его в строку result, если он еще не встречался
    for char in repeating_string:
        if char not in result:
            result += char
    return result
repeating_string = "abc cde def"
output_string = uniques(repeating_string)
print(output_string)


# Посчитать количество строчных (маленьких) и прописных (больших) букв в введенной строке.
# Проверка рассчитана только на английские буквы.
def count_string_capitalization(mixed_string):
# Возвращаем False, если входные данные не строка
    if not isinstance(mixed_string, str):
        return False
# Используем 2 счетчика для прописных и строчных букв
    uppercase_count = 0
    lowercase_count = 0
# Проходим по каждому символу в строке
    for char in mixed_string:
# Проверяем, является ли символ заглавной буквой
        if char.isupper():  
            uppercase_count += 1
# Проверяем, является ли символ строчной буквой
        elif char.islower(): 
            lowercase_count += 1
    return f"В строке '{mixed_string}' {uppercase_count} большие и {lowercase_count} маленькие буквы"
result = count_string_capitalization("This is a sample sentence where the longest word is in the middle!")
print(result)

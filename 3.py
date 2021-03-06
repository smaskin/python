import os
import random
from functools import reduce

# 1. Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
# При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
# В функции необходимо реализовать поиск полного пути по имени файла,
# а затем «выделение» из этого пути имени файла (без расширения).


def get_file_name(path):
    return path.split('/')[-1].split('.')[0]


print(get_file_name('/var/logs/nginx/error.log'))

# 2. Написать программу, которая запрашивает у пользователя ввод числа.
# На введенное число она отвечает сообщением, целое оно или дробное.
# Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
# Если они совпадают, программа должна возвращать значение True, иначе False.


def compare_parts(string):
    try:
        number = float(string)
        if int(number) == number:
            print('целое')
            return None
        else:
            print('дробное')
            left, right = string.split('.')
            return left == right
    except ValueError:
        print('Не число')


print(compare_parts(input('Введите число: ')))

# 3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
# Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
# в словаре для него должно сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.


def get_dictionary(keys, values):
    values.extend([None] * (len(keys) - len(values)))
    return {key: value for (key, value) in zip(keys, values)}


print(get_dictionary([3, 7, 45, 76], [44, 66]))

# 4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение.
# Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
# Для создания списков использовать генераторы. Применить к спискам функцию zip().
# Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
# чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
# В нее должна передаваться ссылка на созданный файл.
# Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
# Вся программа должна запускаться по вызову первой функции.


LINES_COUNT = STRING_SIZE = 10


def get_random_string():
    return reduce(lambda string, char: string + char, [chr(random.randint(ord('a'), ord('z'))) for _ in range(STRING_SIZE)])


def create_text_file(name):
    if os.path.isfile(name):
        print('Файл с таким именем уже существует')
        return False
    with open(name, 'w', encoding='utf-8') as d:
        numbers = [random.randint(0, 100) for _ in range(LINES_COUNT)]
        strings = [get_random_string() for _ in range(LINES_COUNT)]
        d.writelines(['{} {}\n'.format(number, text) for number, text in zip(numbers, strings)])
        return d


def print_text_file(desc):
    with open(desc.name, 'r', encoding='utf-8') as d:
        for line in d:
            print(line)


descriptor = create_text_file('newfile.txt')
if descriptor:
    print_text_file(descriptor)


# 5. Усовершенствовать первую функцию из предыдущего примера.
# Необходимо во втором списке часть строковых значений заменить на значения типа example345 (строка+число).
# Далее — усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям: вывод первого вхождения,
# вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод всех подстрок,
# состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.

# Не понял задание

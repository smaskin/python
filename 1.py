import os

# 1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
# Первый и второй множитель должны задаваться в виде аргументов функции.
# Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
# После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
# Полученная строка выводится в главной функции.
# Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.


def table(length, height):
    for i in range(height + 1):
        row = []
        for j in range(length + 1):
            if i == 0:
                row.append(j)
            elif j == 0:
                row.append(i)
            else:
                row.append(i * j)
        print('\t'.join([str(i) for i in row]))


table(14, 5)


# 2. Дополнить следующую функцию недостающим кодом:

def print_directory_contents(sPath):
    """
    Функция принимает имя каталога и распечатывает его содержимое
    в виде «путь и имя файла», а также любые другие
    файлы во вложенных каталогах.

    Эта функция подобна os.walk. Использовать функцию os.walk
    нельзя. Данная задача показывает ваше умение работать с
    вложенными структурами.
    """
    def get_directory_files(sPath):
        struct = []
        for file_or_directory in os.listdir(sPath):
            full_name = os.path.join(os.path.abspath(sPath), file_or_directory)
            if os.path.isfile(full_name):
                struct.append((os.path.abspath(sPath), file_or_directory))
            else:
                struct.extend(get_directory_files(full_name))
        return struct
    return print(get_directory_files(sPath))


print_directory_contents('/var/log')


# 3. Разработать генератор случайных чисел.
# В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
# Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
# Вывести содержимое созданных списка и словаря.
import random


def gen(start, finish):
    spisok = []
    slovar = {}
    for _ in range(10):
        rnd = int((finish - start) * random.random() + start)
        spisok.append(rnd)
        slovar.update({'elem_{}'.format(rnd): rnd})

    return (spisok, slovar)


print(gen(7, 26))


# 4. Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами.
# Клиент банка делает депозит на определенный срок.
# В зависимости от суммы и срока вклада определяется процентная ставка:
# 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
# 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
# 100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
# Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада.
# Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
# Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока.
# В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и выполнять расчет по
# нужной процентной ставке.
# Функция возвращает сумму вклада на конец срока.

def get_percent(amount, months):
    if months not in [6, 12, 24]:
        return False

    rates = (
        {'begin_sum': 1000, 'end_sum': 10000, 6: 5, 12: 6, 24: 5},
        {'begin_sum': 10000, 'end_sum': 100000, 6: 6, 12: 7, 24: 6.5},
        {'begin_sum': 100000, 'end_sum': 1000000, 6: 7, 12: 8, 24: 7.5},
    )

    for rate in rates:
        if rate['begin_sum'] <= amount < rate['end_sum']:
            return rate[months]

    return False


def deposit(amount, months):
    percent = get_percent(amount, months)
    if not percent:
        print('Нет подходящего тарифа')

    total = amount
    for month in range(months):
        profit = total * percent / 100 / 12
        total += profit

    print(round(total, 2))


deposit(10000, 24)

# 5. Усовершенствовать программу «Банковский депозит».
# Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
# Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
# Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
# Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
# Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
# а главная функция — общую сумму по вкладу на конец периода.


def chargable_deposit(amount, months, charge=0):
    percent = get_percent(amount, months)
    if not percent:
        print('Нет подходящего тарифа')

    total = amount
    for month in range(months):
        profit = total * percent / 100 / 12
        total += profit
        if month != 0 and month != months - 1:
            total += charge + charge * percent / 100 / 12

    print(round(total, 2))


chargable_deposit(10000, 24, 100)

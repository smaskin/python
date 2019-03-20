# 1. Проверить механизм наследования в Python. Для этого создать два класса. Первый — родительский (ItemDiscount),
# должен содержать статическую информацию о товаре: название и цену. Второй — дочерний (ItemDiscountReport),
# должен содержать функцию (get_parent_data), отвечающую за отображение информации о товаре в одной строке.
# Проверить работу программы, создав экземпляр (объект) родительского класса.


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.name, self.price)


child = ItemDiscountReport('sale', 10)
print(child.get_parent_data())

# 2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
# Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.__name, self.__price)


child = ItemDiscountReport('sale', 10)
print(child.get_parent_data())

# 3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
# Результат выполнения заданий 1 и 2 должен быть идентичным.


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_parent_data(self):
        print(self.__name, self.__price)


child = ItemDiscountReport('sale', 10)
print(child.get_parent_data())

# 4. Реализовать возможность переустановки значения цены товара.
# Необходимо, чтобы и родительский, и дочерний классы получили новое значение цены.
# Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего (функция,
# отвечающая за отображение информации о товаре в одной строке).


class ItemDiscount:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_price(self, price):
        self.__price = price

    def get_parent_data(self):
        print(self.__name, self.__price)


child = ItemDiscountReport('sale', 10)
child.set_price(30)
print(child.get_parent_data())


# 5. Реализовать расчет цены товара со скидкой.
# Величина скидки должна передаваться в качестве аргумента в дочерний класс.
# Выполнить перегрузку методов конструктора дочернего класса
# (метод init, в который должна передаваться переменная — скидка), и перегрузку метода str дочернего класса.
# В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
# Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
# (вторая и третья строка после объявления дочернего класса).


class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReport(ItemDiscount):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def __str__(self):
        return f'{self.name} {self.price - self.discount}'


child = ItemDiscountReport('sale', 10, 1)
print(child)


# 6. Проверить на практике возможности полиморфизма.
# Необходимо разделить дочерний класс ItemDiscountReport на два класса. Инициализировать классы необязательно.
# Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара,
# а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.

class ItemDiscount:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class ItemDiscountReportOne(ItemDiscount):
    def get_info(self):
        print(self.name)


class ItemDiscountReportTwo(ItemDiscount):
    def get_info(self):
        print(self.price)


one = ItemDiscountReportOne('sale', 5)
one.get_info()

two = ItemDiscountReportTwo('wholesale', 10)
two.get_info()

for obj in (one, two):
    obj.get_info()


def obj_handler(obj):
    obj.get_info()


obj_handler(one)
obj_handler(two)

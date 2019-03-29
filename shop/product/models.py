from django.db import models


class Product(models.Model):
    UNITS = (
        (1, 'шт.'),
        (2, 'кг.'),
    )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"

    name = models.CharField(verbose_name='название', max_length=128)
    date = models.DateField(verbose_name='дату поступления')
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=0, default=0)
    unit = models.IntegerField(verbose_name='еденица измерения', choices=UNITS)
    provider = models.CharField(verbose_name='имя поставщика', max_length=256, blank=True)

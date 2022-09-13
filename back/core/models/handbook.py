from django.db import models


class Rating(models.Model):

    rating = models.CharField(max_length=10, null=True, unique=True, db_index=True, verbose_name='Обозначение')

    class Meta:
        db_table = 'rating'
        verbose_name = 'Рейтинг контрагента'
        verbose_name_plural = 'Рейтинги контрагентов'

    def __str__(self):
        return str(self.rating)


class DealType(models.Model):

    name = models.CharField(max_length=255, null=True, unique=True, db_index=True, verbose_name='Название')

    class Meta:
        db_table = 'deal_type'
        verbose_name = 'Тип сделки'
        verbose_name_plural = 'Типы сделок'

    def __str__(self):
        return str(self.name)


class Place(models.Model):

    name = models.CharField(max_length=255, null=True, unique=True, db_index=True, verbose_name='Адрес')

    class Meta:
        db_table = 'place'
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return str(self.name)


class Inventory(models.Model):

    name = models.CharField(max_length=255, null=True, unique=True, db_index=True, verbose_name='Название')

    class Meta:
        db_table = 'inventory'
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'

    def __str__(self):
        return str(self.name)

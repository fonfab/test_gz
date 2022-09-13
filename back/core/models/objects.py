from django.db import models
from django.utils import timezone

from . import handbook

# Create your models here.


class Counterparty(models.Model):

    name = models.CharField(max_length=255, null=True, unique=True, db_index=True, verbose_name='Название')
    rating = models.ForeignKey(handbook.Rating, null=True, on_delete=models.SET_NULL, verbose_name='Рейтинг')

    class Meta:
        db_table = 'counterparty'
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'

    def __str__(self):
        return f'{str(self.name)} ({str(self.rating)})'


class Deal(models.Model):

    type = models.ForeignKey(handbook.DealType, null=True, on_delete=models.SET_NULL, verbose_name='Тип')

    deal_date = models.DateTimeField(default=timezone.now(), verbose_name='Дата сделки')

    destination_place = models.ForeignKey(
        handbook.Place, null=True, on_delete=models.SET_NULL, verbose_name='Пункт поставки')

    amount = models.FloatField(default=0, verbose_name='Объем')
    cost = models.FloatField(default=0, verbose_name='Цена')

    start_date = models.DateTimeField(default=timezone.now(), verbose_name='Начало поставки')
    end_date = models.DateTimeField(default=timezone.now(), null=True, verbose_name='Конец поставки')

    inventory = models.ForeignKey(handbook.Inventory, null=True, on_delete=models.SET_NULL, verbose_name='Инструмент')
    counterparty = models.ForeignKey(Counterparty, null=True, on_delete=models.SET_NULL, verbose_name='Контрагент')

    class Meta:
        db_table = 'deal'
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'
        unique_together=['type', 'deal_date', 'destination_place']

    def __str__(self):
        return f'{str(type)} {str(self.destination_place)} {str(self.deal_date)}'

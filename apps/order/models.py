from django.db import models


class Order(models.Model):
    ORDERING = (
        (0, 'Самовызов'),
        (1, 'Доставка Курьером'),
    )
    PAY = (
        (0, 'Банковская карта'),
        (1, 'Наличными'),
        (2, 'Apple pay'),
        (3, 'Google pay'),
        (4, 'Криптовалюта'),
        (5, 'С расчетного счета'),
    )
    name = models.CharField(max_length=221)
    number = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    number_reciever = models.CharField(max_length=25, null=True, blank=True)
    name_reciever = models.CharField(max_length=221, null=True, blank=True)
    commentary = models.TextField(null=True, blank=True)
    ordering = models.IntegerField(choices=ORDERING, default=0)
    city = models.CharField(max_length=221)
    street = models.CharField(max_length=221)
    structure = models.CharField(max_length=221)  # корп/стр
    house = models.IntegerField(default=0)
    office = models.CharField(max_length=221)  # кв/офис
    time_ordering = models.DateField()  # время доставки
    pay = models.IntegerField(choices=PAY, default=1)
    promocode = models.CharField(max_length=221, null=True, blank=True)

    def __str__(self):
        return f"{self.name}'s order in {self.city}/{self.street}"
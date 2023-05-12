# Generated by Django 4.2.1 on 2023-05-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=221)),
                ('number', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('number_reciever', models.CharField(blank=True, max_length=25, null=True)),
                ('name_reciever', models.CharField(blank=True, max_length=221, null=True)),
                ('commentary', models.TextField(blank=True, null=True)),
                ('ordering', models.IntegerField(choices=[(0, 'Самовызов'), (1, 'Доставка Курьером')], default=0)),
                ('city', models.CharField(max_length=221)),
                ('street', models.CharField(max_length=221)),
                ('structure', models.CharField(max_length=221)),
                ('house', models.IntegerField(default=0)),
                ('office', models.CharField(max_length=221)),
                ('time_ordering', models.DateField()),
                ('pay', models.IntegerField(choices=[(0, 'Банковская карта'), (1, 'Наличными'), (2, 'Apple pay'), (3, 'Google pay'), (4, 'Криптовалюта'), (5, 'С расчетного счета')], default=1)),
                ('promocode', models.CharField(blank=True, max_length=221, null=True)),
            ],
        ),
    ]

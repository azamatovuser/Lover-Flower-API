# Generated by Django 4.2.1 on 2023-05-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rate',
            field=models.IntegerField(choices=[(0, '⭐️'), (1, '⭐️⭐️'), (2, '⭐️⭐️⭐️'), (3, '⭐️⭐️⭐️⭐️'), (4, '⭐️⭐️⭐️⭐️⭐️')], default=0),
        ),
    ]

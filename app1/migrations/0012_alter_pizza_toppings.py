# Generated by Django 3.2.5 on 2021-08-11 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_pizza_topping'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(related_name='pizzas', to='app1.Topping'),
        ),
    ]

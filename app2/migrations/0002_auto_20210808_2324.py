# Generated by Django 3.2.5 on 2021-08-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='address',
            new_name='addr',
        ),
        migrations.AddField(
            model_name='person',
            name='company',
            field=models.CharField(default='Infosys', max_length=100),
        ),
    ]

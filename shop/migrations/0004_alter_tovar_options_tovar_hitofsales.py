# Generated by Django 4.0.5 on 2022-06-17 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_alter_productitemimage_options_alter_tovar_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tovar',
            options={'ordering': ('nametovar',), 'verbose_name_plural': 'Товар'},
        ),
        migrations.AddField(
            model_name='tovar',
            name='hitofsales',
            field=models.BooleanField(default=1, verbose_name='Хит продаж'),
            preserve_default=False,
        ),
    ]

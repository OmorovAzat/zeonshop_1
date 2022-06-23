# Generated by Django 4.0.5 on 2022-06-22 05:30

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_alter_cartitem_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='color_item_cart',
            field=colorfield.fields.ColorField(choices=[('#FFFFFF', 'white'), ('#000000', 'black'), ('#FF0000', 'red'), ('#00FF00', 'lime'), ('#0000FF', 'blue'), ('#FFFF00', 'yellow'), ('#808080', 'gray'), ('#000080', 'navy')], default='#FFFFFF', image_field=None, max_length=18, samples=None, verbose_name='Цвет товара'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='price_cart',
            field=models.IntegerField(blank=True, null=True, verbose_name='Сумма всех линеек'),
        ),
    ]

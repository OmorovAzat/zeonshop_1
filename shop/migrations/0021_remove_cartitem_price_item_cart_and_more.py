# Generated by Django 4.0.5 on 2022-06-22 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_cart_color_item_cart_cartitem_price_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='price_item_cart',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='oldpirce_item',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Старая Цена'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='price_item',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Цена'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='size_item',
            field=models.CharField(blank=True, max_length=100, verbose_name='Размер'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity_item_lines',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество всхе линеек'),
        ),
    ]

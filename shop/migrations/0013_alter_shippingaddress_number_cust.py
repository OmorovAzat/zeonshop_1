# Generated by Django 4.0.5 on 2022-06-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_cart_options_alter_cartitem_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='number_cust',
            field=models.CharField(blank=True, max_length=100, verbose_name='Номер Телефона'),
        ),
    ]
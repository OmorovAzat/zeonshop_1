# Generated by Django 4.0.5 on 2022-06-21 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_shippingaddress_number_cust'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cart_product', to='shop.tovar'),
            preserve_default=False,
        ),
    ]
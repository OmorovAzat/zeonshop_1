# Generated by Django 4.0.5 on 2022-06-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_cart_image_cart_alter_cart_name_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vybor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heder', models.ImageField(blank=True, upload_to='None/%Y/%m/%d', verbose_name='Логотип для Хедера')),
                ('foter', models.ImageField(blank=True, upload_to='None/%Y/%m/%d', verbose_name='Логотип для Футера')),
                ('info_footer', models.CharField(blank=True, max_length=100, null=True, verbose_name='Инфо')),
            ],
        ),
        migrations.RemoveField(
            model_name='footer',
            name='foter',
        ),
        migrations.RemoveField(
            model_name='footer',
            name='heder',
        ),
    ]
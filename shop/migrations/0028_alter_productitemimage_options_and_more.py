# Generated by Django 4.0.5 on 2022-06-24 08:46

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_tovaritem_productitemimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productitemimage',
            options={},
        ),
        migrations.RemoveField(
            model_name='tovar',
            name='colortovar',
        ),
        migrations.RemoveField(
            model_name='tovar',
            name='image_item',
        ),
        migrations.AddField(
            model_name='productitemimage',
            name='colortovar',
            field=colorfield.fields.ColorField(choices=[('#FFFFFF', 'white'), ('#000000', 'black'), ('#FF0000', 'red'), ('#00FF00', 'lime'), ('#0000FF', 'blue'), ('#FFFF00', 'yellow'), ('#808080', 'gray'), ('#000080', 'navy')], default='#FFFFFF', image_field=None, max_length=18, samples=None),
        ),
        migrations.DeleteModel(
            name='TovarItem',
        ),
    ]
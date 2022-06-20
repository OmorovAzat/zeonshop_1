from rest_framework import serializers

from .models import Prem, Onas, Public, Help, News, Category, Slider, Svyaz, Tovar, ProductItemImage, TovarItem, Footer, \
    Vybor


# Наши преимущества

class PremSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prem
        fields = ('icon', 'zagalovok', 'description')


# О нас
class OnasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Onas
        fields = ('zaga', 'opisanie', 'photo1', 'photo2', 'photo3')


# Публичная оферта
class PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = ('ugolok', 'opisanie')


# Новости
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('photonews', 'zaganews', 'opisanie')


# Коллекция
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'photocolect', 'title']


# Слайдер
class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('sliderpole', 'sliderpu')


# Обратный звонок
class SvyazSerializer(serializers.ModelSerializer):
    class Meta:
        model = Svyaz
        fields = ('namepole', 'numberpole', 'vremya', 'stazvonili',)


class TovarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TovarItem
        fields = ('colortovar',)


class ProductItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItemImage
        fields = ('image',)


class TovarSerializer(serializers.ModelSerializer):
    class Meta:
        product_item_image = ProductItemImageSerializer(many=True, read_only=True)
        tovar = TovarItemSerializer(many=True, read_only=True)
        model = Tovar
        fields = ('id', 'category', 'slug', 'nametovar', 'pricetovar', 'imagetovar', 'old_price', 'pricediscount',
                  'size_range', 'descriptiontovar', 'articul', 'material', 'tkan', 'poiskizbrannye', 'hitofsales',
                  'newtov', 'quantity_inline_tovar')


class SimpleTovarSerializer(serializers.ModelSerializer):
    class Meta:
        product_item_image = ProductItemImageSerializer(many=True, read_only=True)
        tovar = TovarItemSerializer(many=True, read_only=True)
        model = Tovar
    fields = ('id', 'category', 'nametovar', 'pricetovar', 'old_price', 'pricediscount')


# Поиск
class PoiskSerializer(serializers.ModelSerializer):
    # product_item_image = ProductItemImageSerializer(many=True, read_only=True)
    # tovar = TovarItemSerializer(many=True, read_only=True)

    class Meta:
        model = Tovar
        fields = (
            'id','nametovar', 'category', 'nametovar', 'pricetovar', 'old_price', 'pricediscount',
            'poiskizbrannye', 'hitofsales', 'newtov','imagetovar')


'''Помощь'''
class HelpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Help
        fields = ('question', 'answer', 'pucture')

class FooterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footer
        fields = ('info', 'heder', 'foter',
                  'numheder', 'telnum', 'mail',
                  'insta', 'tele', 'wats')


"""Выборка ватс телеграм"""
class VyborSerlializer(serializers.ModelSerializer):
    class Meta:
        model = Vybor
        fields = ('wats', 'tele')




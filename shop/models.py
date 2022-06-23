from django.core.exceptions import ValidationError
from django.db import models
from ckeditor.fields import RichTextField
from colorfield.fields import ColorField
from setuptools._entry_points import _
from multiselectfield import MultiSelectField

COLOR_PALETTE = [
    ("#FFFFFF", "white",),
    ("#000000", "black",),
    ("#FF0000", "red",),
    ("#00FF00", "lime",),
    ("#0000FF", "blue",),
    ("#FFFF00", "yellow",),
    ("#808080", "gray",),
    ("#000080", "navy",),
]

CONTACT = [
    ('Number', 'Number',),
    ('Mail', 'Mail',),
    ('Instagram', 'Instagram',),
    ('Telegram', 'Telegram',),
    ('WhatsApp', 'WhatsApp',),
]


# Примушества
class Prem(models.Model):
    icon = models.FileField(upload_to=None, max_length=95,
                            verbose_name='Фото')
    zagalovok = models.TextField(max_length=150, verbose_name='Заголовок')
    description = RichTextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name_plural = "Преимущества"

    def __str__(self):
        return self.zagalovok


# О нас
class Onas(models.Model):
    zaga = models.TextField(max_length=150, verbose_name='Заголовок')
    opisanie = RichTextField(blank=True, verbose_name='Описание')

    photo1 = models.ImageField(upload_to=None,
                               height_field=None, width_field=None)
    photo2 = models.ImageField(upload_to=None,
                               height_field=None, width_field=None)
    photo3 = models.ImageField(upload_to=None,
                               height_field=None, width_field=None)

    class Meta:
        verbose_name_plural = "О нас"

    def __str__(self):
        return self.zaga


# Помощь

class Help(models.Model):
    question = models.TextField(max_length=150, verbose_name='Вопрос')
    answer = models.TextField(max_length=150, verbose_name='Ответ')
    pucture = models.ImageField(height_field=None, width_field=None,
                                max_length=100, verbose_name='Фото для помощи')

    class Meta:
        verbose_name_plural = "Помощь"

    def __str__(self):
        return self.question


# Публичная оферта

class Public(models.Model):
    ugolok = models.TextField(max_length=150, verbose_name='Заголовок')
    opisanie = RichTextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name_plural = "Публичный оферта"

    def __str__(self):
        return self.ugolok


# Новости

class News(models.Model):
    photonews = models.ImageField(upload_to=None,
                                  height_field=None, width_field=None,
                                  max_length=100,
                                  verbose_name='Фотография для новостей')
    zaganews = models.TextField(max_length=200, verbose_name='Заголовок')
    opisanie = RichTextField(blank=True, verbose_name='Описание')

    class Meta:
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.zaganews


# Коллекция

class Category(models.Model):
    photocolect = models.ImageField(upload_to=None,
                                    height_field=None,
                                    width_field=None,
                                    max_length=100,
                                    verbose_name='Фото для Коллеции')
    title = models.TextField(max_length=200, verbose_name='Заголовок')

    class Meta:
        verbose_name_plural = "Коллекция"

    def __str__(self):
        return self.title


# Слайдер

class Slider(models.Model):
    sliderpole = models.ImageField(upload_to=None,
                                   height_field=None,
                                   width_field=None,
                                   max_length=100,
                                   verbose_name='Фото для Слайдера')
    sliderpu = models.URLField(null=True, blank=True, max_length=200, )

    def __str__(self):
        return str(self.sliderpole)

    class Meta:
        verbose_name_plural = "Слайдер"


# Обратная связь

class Svyaz(models.Model):
    namepole = models.CharField(max_length=100, blank=True, verbose_name='Имя')
    numberpole = models.CharField(max_length=200,
                                  verbose_name='Номер телефона')
    vremya = models.DateTimeField(auto_now=True)
    stazvonili = models.BooleanField(default=None,
                                     verbose_name='Cтатус позвонили')

    class Meta:
        verbose_name_plural = "Обратный звонок с фронта"

    def __str__(self):
        return self.namepole


"""Товары"""


class Tovar(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='tovars',
                                 on_delete=models.CASCADE)
    slug = models.SlugField(max_length=250, editable=False, db_index=True)
    imagetovar = models.ImageField(upload_to='None/%Y/%m/%d',
                                   verbose_name='Фотографии')
    nametovar = models.CharField(max_length=150,
                                 verbose_name='Название товара')
    articul = models.CharField(max_length=150, verbose_name='Aртикул')
    pricetovar = models.IntegerField(blank=True, verbose_name='Цена')
    old_price = models.IntegerField(verbose_name='Старая Цена')
    pricediscount = models.IntegerField(verbose_name='Процент скидки')
    descriptiontovar = RichTextField(verbose_name='Описание Товара')
    size_range = models.CharField(max_length=100, null=True,
                                  blank=True, verbose_name='Размерный ряд')
    tkan = models.CharField(max_length=200, verbose_name='Состав ткани')
    quantity_inline_tovar = models.IntegerField(
        verbose_name='Кол-во в линейке')
    material = models.CharField(max_length=155, verbose_name='Материал')
    poiskizbrannye = models.BooleanField(verbose_name='Избранные')
    hitofsales = models.BooleanField(verbose_name='Хит продаж')
    newtov = models.BooleanField(verbose_name='Новинки')
    colortovar = ColorField(choices=COLOR_PALETTE, verbose_name='Цвет товару')
    image_item = models.ImageField(upload_to='None/%Y/%m/%d',
                                   null=True, blank=True)

    def __str__(self):
        return str(self.nametovar)

    def save(self, *args, **kwargs):
        if self.pricediscount:
            self.pricetovar = int(self.old_price *
                                  (100 - self.pricediscount) / 100)
            self.quantity_inline_tovar = (int(self.size_range[3:]) - int(self.size_range[0:2]) + 2) // 2
            print(self.size_range)
        else:
            self.pricetovar = None
        super(Tovar, self).save(*args, *kwargs)

    class Meta:
        verbose_name_plural = "Товар"
        ordering = ('nametovar',)


# class TovarItem(models.Model):
#     TovarItem = models.ForeignKey(Tovar,
#     related_name='tovar',
#     on_delete=models.CASCADE)
#
#     colortovar = ColorField(choices=COLOR_PALETTE)
#
#     class Meta:
#         verbose_name_plural = "Цвет товара"
#
#     def __str__(self):
#         return str(self.colortovar)


# Фотография


def validate_even(value):
    if value == 2:
        raise ValidationError(
            _('%(value)s не является четным числом'),
            params={'value': value},
        )


# class ProductItemImage(models.Model):
#     product = models.ForeignKey(Tovar,
#     on_delete=models.CASCADE,
#     related_name='product_item_image')
#     image = models.ImageField(upload_to='None/%Y/%m/%d',
#     null=True, blank=True,
#     validators=[validate_even])
#
#     class Meta:
#         verbose_name_plural = "Фото для продукта"
#
#     def __str__(self):
#         return str(self.product)

"""Выборка Футера"""


class Footer(models.Model):
    info = models.CharField(max_length=100,
                            null=True, blank=True,
                            verbose_name='Инфо о контакте')
    numheder = models.IntegerField(blank=True, verbose_name='Номер в хедере')
    contacts = MultiSelectField(choices=CONTACT,
                                max_length=150, max_choices=150,
                                verbose_name='Выбор из списка')
    telnum = models.CharField(max_length=100, blank=True, verbose_name='Номер')
    mail = models.EmailField(max_length=100, verbose_name='Почта')
    insta = models.CharField(max_length=100,
                             null=True, blank=True,
                             verbose_name='Инстаграм')
    tele = models.CharField(max_length=100,
                            null=True, blank=True,
                            verbose_name='Телеграм')
    wats = models.CharField(max_length=100, null=True,
                            blank=True, verbose_name='Ватсап')

    def save(self, *args, **kwargs):
        if 'WhatsApp' in self.contacts:
            self.wats = f'https://wa.me/{self.wats}/'
        if 'Telegram' in self.contacts:
            self.tele = f'https://t.me/{self.tele}/'
        elif 'Instagram' in self.contacts:
            self.insta = f'https://www.instagram.com/{self.insta}/'
        elif 'Mail' in self.contacts:
            self.mail = f'https://mail.doodle.com/{self.mail}/'
        elif 'Number' in self.contacts:
            self.telnum = f'+996{self.telnum}'

        super(Footer, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.contacts)

    class Meta:
        verbose_name_plural = 'Футер и Хедер'


"""Хедер и Футер"""


class Vybor(models.Model):
    heder = models.ImageField(upload_to='None/%Y/%m/%d',
                              blank=True, verbose_name='Логотип для Хедера')
    foter = models.ImageField(upload_to='None/%Y/%m/%d',
                              blank=True, verbose_name='Логотип для Футера')
    info_footer = models.CharField(max_length=100, null=True,
                                   blank=True, verbose_name='Инфо')

    class Meta:
        verbose_name_plural = 'Лого и номер футера'

    def __str__(self):
        return str(self.info_footer)


#
#     def __str__(self):
#         return self.contacts

"""Корзина"""


class Cart(models.Model):
    product = models.ForeignKey(Tovar, on_delete=models.CASCADE,
                                related_name='cart_product', blank=True)
    image_cart = models.ImageField(upload_to='None/%Y/%m/%d',
                                   blank=True, verbose_name='Фото товара')
    color_item_cart = ColorField(choices=COLOR_PALETTE,
                                 verbose_name='Цвет товара')
    price_item = models.IntegerField(blank=True, verbose_name='Цена')
    quantity_item = models.IntegerField(default=1, null=True, blank=True,
                                        verbose_name='Количество Товара')
    quantity_inline_tovar = models.IntegerField(verbose_name='К-во в линейке')

    def __str__(self):
        return str(self.product)

    class Meta:
        verbose_name_plural = 'Корзина'


Status = (
    ('Оформлен', 'Оформлен'),
    ('Отменен', 'Отменен'),
    ('Новый', 'Новый'),

)
"""Инфо о покупателя"""


class ShippingAddress(models.Model):
    name_cust = models.CharField(max_length=100,
                                 blank=True, verbose_name='Имя')
    firs_cust = models.CharField(max_length=100,
                                 blank=True, verbose_name='Фамилия')
    email_customer = models.EmailField(max_length=254, verbose_name='Почта')
    number_cust = models.CharField(max_length=100,
                                   blank=True, verbose_name='Номер Телефона')
    country = models.CharField(max_length=200,
                               null=True, verbose_name='Страна')
    city = models.CharField(max_length=200, null=True, verbose_name='Город')
    date_added = models.DateTimeField(auto_now_add=True)
    choice_contact = MultiSelectField(choices=Status,
                                      max_length=150, max_choices=150,
                                      default=('Новый', 'Новый'),
                                      verbose_name='Выбор из списка')

    class Meta:
        verbose_name_plural = 'Адрес доставки'

    def __str__(self):
        return str(self.country)


"""Оформление Заказа"""


class CartItem(models.Model):
    cart = models.ManyToManyField(Cart, related_name='custom_cart', blank=True)
    price_item = models.IntegerField(null=True,
                                     blank=True,
                                     default=0, verbose_name='Цена')
    oldpirce_item = models.IntegerField(null=True,
                                        blank=True,
                                        default=0,
                                        verbose_name='Старая Цена')
    sale_item_cart = models.IntegerField(null=True,
                                         blank=True,
                                         default=0,
                                         verbose_name='Скидка')
    quantity_item = models.IntegerField(default=1,
                                        null=True, blank=True,
                                        verbose_name='Количество Товара')
    quantity_item_lines = models.IntegerField(null=True,
                                              blank=True, default=0,
                                              verbose_name='Кв-о всех линеек')
    quantity_inline_tovar = models.IntegerField(null=True,
                                                blank=True,
                                                verbose_name='К-во в линейке')
    quantity_cart_lines = models.IntegerField(null=True,
                                              blank=True,
                                              default=0,
                                              verbose_name='К-во всехтов в лке')
    price_cart = models.IntegerField(null=True,
                                     blank=True,
                                     verbose_name='Сумма всех линеек')
    sale_item = models.IntegerField(null=True,
                                    blank=True, default=0,
                                    verbose_name='Сумма всех скидок')
    result_price = models.IntegerField(null=True,
                                       blank=True, default=0,
                                       verbose_name='Итого к оплате')
    user = models.ForeignKey(ShippingAddress,
                             on_delete=models.CASCADE, null=True,
                             related_name='user', blank=True)

    def save(self, *args, **kwargs):
        self.price_item = self.oldpirce_item * self.quantity_item_lines
        self.quantity_item_lines = int(self.quantity_inline_tovar * self.quantity_item_lines)
        self.sale_item_cart = (self.oldpirce_item - self.price_item) * self.quantity_item
        self.result_price = self.price_item * self.quantity_item_lines
        super().save(*args, *kwargs)

    def __str__(self):
        return str(self.cart)

    class Meta:
        verbose_name_plural = 'Оформление заказа'

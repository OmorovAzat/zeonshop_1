from django.contrib import admin

from .models import Prem, Onas, Help, Public, News, Category, Slider, Svyaz, Tovar, ProductItemImage, Footer, \
    Vybor
from .serializers import TovarItem

admin.site.register(Prem),
admin.site.register(Onas),
admin.site.register(Help),
admin.site.register(Public),
admin.site.register(News),
admin.site.register(Category),
admin.site.register(Slider),
admin.site.register(Svyaz),
admin.site.register(Tovar),
admin.site.register(ProductItemImage),
admin.site.register(TovarItem)
admin.site.register(Footer)
admin.site.register(Vybor)


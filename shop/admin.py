from django.contrib import admin

from .models import Prem, Onas, Help, Public, News, Category, Slider, Svyaz, Tovar, Footer, Cart, CartItem, \
    ShippingAddress, ProductItemImage, Vybor

# from .serializers import TovarItem

admin.site.register(Public),
admin.site.register(News),
admin.site.register(Category),
admin.site.register(Svyaz),
admin.site.register(Cart)
admin.site.register(CartItem)

admin.site.register(ShippingAddress)


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Onas)
class OnasAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(Help)
class HelpAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

@admin.register(Vybor)
class VyborAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

@admin.register(Prem)
class PremAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


class TovarInline(admin.TabularInline):
    model = ProductItemImage
    min_num = 1
    max_num = 8


class ProductItemImageAdmin(admin.ModelAdmin):
    inlines = [
        TovarInline
    ]


admin.site.register(Tovar, ProductItemImageAdmin)

from django.contrib import admin
from django.urls import path, include

from shop.views import PremApiView, OnasApiView, HelpApiView, PublicApiView, NewsApiView, CategoryListApiView, \
    SliderApiView, SvyazApiView, TovarApiView, PoiskApiViewfilter, FooterApiView, CartItemApiView, VyborApiView,\
    TovarRandomView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', PremApiView.as_view()),
    path('api/v2/', OnasApiView.as_view()),
    path('api/v3/', HelpApiView.as_view()),
    path('api/v4/', PublicApiView.as_view()),
    path('api/v5/', NewsApiView.as_view()),
    path('api/v6/', CategoryListApiView.as_view()),
    path('api/v7/', SliderApiView.as_view()),
    path('api/v8/', SvyazApiView.as_view()),
    path('api/v9/', TovarApiView.as_view()),
    path('api/v10/nametovar/', PoiskApiViewfilter.as_view()),
    # path('api1/v11/<str:pk>/', SearchApi),
    path('api/v11/', FooterApiView.as_view()),
    path('api/v12/', VyborApiView.as_view()),
    path('cart-items', CartItemApiView.as_view()),
    path('cart-items/<int:id>', CartItemApiView.as_view()),
    path('api/v13/', TovarRandomView.as_view()),

]

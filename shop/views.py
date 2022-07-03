import random
from random import choice

from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from rest_framework import generics, pagination, filters, status
from rest_framework.views import APIView

from .models import Prem, Help, Public, \
    News, Category, Slider, Svyaz, Onas, Tovar, \
    Footer, CartItem, ShippingAddress, \
    Vybor, ProductItemImage, Cart

from .serializers import PremSerializer, HelpSerializer, \
    PublicSerializer, NewsSerializer, \
    CategorySerializer, SliderSerializer, \
    SvyazSerializer, OnasSerializer, \
    PoiskSerializer, TovarSerializer, \
    FooterSerializer, CartItemSerializer, \
    ShippingAddressSerializer, VyborSerializer, \
    ProductItemImageSerializer, CartSerializer


class PremApiView(generics.ListAPIView):
    queryset = Prem.objects.all()
    serializer_class = PremSerializer


class OnasApiView(generics.ListAPIView):
    queryset = Onas.objects.all()
    serializer_class = OnasSerializer


class ProductItemImageApiView(generics.ListAPIView):
    queryset = ProductItemImage.objects.all()
    serializer_class = ProductItemImageSerializer


class HelpApiView(generics.ListAPIView):
    queryset = Help.objects.all()
    serializer_class = HelpSerializer


class PublicApiView(generics.ListAPIView):
    queryset = Public.objects.all()
    serializer_class = PublicSerializer


class CustomPagination(pagination.PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'p'


class NewsApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


class CustoPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'p'


class CategoryListApiView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustoPagination


class SliderApiView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class SvyazApiView(generics.ListAPIView):
    queryset = Svyaz.objects.all()
    serializer_class = SvyazSerializer


class CustPagination(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100
    page_query_param = 'p'


class PoiskApiViewfilter(generics.ListAPIView):
    queryset = Tovar.objects.all().order_by('-id')
    serializer_class = PoiskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nametovar']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        if not queryset:
            try:
                category = list(Category.objects.values_list
                                ('id', flat=True).order_by('?'))
                queryset = list(random.choice
                                (self.queryset.filter(category=pk))
                                for pk in category)[:5]
                serializer = \
                    self.serializer_class(queryset,
                                          many=True,
                                          context={'context': request})
                return Response(serializer.data)
            except IndexError:
                queryset = self.queryset.order_by('?')[:5]
                serializer = \
                    self.serializer_class(queryset,
                                          many=True,
                                          context={'context': request})
                return Response(serializer.data)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FooterApiView(generics.ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer


class VyborApiView(generics.ListAPIView):
    queryset = Vybor.objects.all()
    serializer_class = VyborSerializer


class TovarApiView(generics.ListAPIView):
    queryset = Tovar.objects.all()
    serializer_class = TovarSerializer


class SliderApiView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class ShippingAddressApiView(generics.ListAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

    def post(self, request, id=id):
        serializer = ShippingAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class CartItemApiView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def post(self, request, id=id):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        before_discount = Cart.total_before_discound()
        after_discount = Cart.total_price_after_discound()
        discount = before_discount - after_discount
        products = Cart.quantity_tovarov()
        lines = Cart.total_quantity()

        return Response({'Сумма до скидки': before_discount,
                         'Сумма после скидки': after_discount,
                         'Скидка': discount,
                         'Количество всех товаров в линейке': products,
                         'Количество всех линеек': lines})

    def delete(self, request, id=id):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Успешно удалено!"})


class CartApiView(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def post(self, request, id=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

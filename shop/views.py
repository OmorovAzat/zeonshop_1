from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics, pagination, filters, status
from rest_framework.decorators import api_view

from .models import Prem, Help, Public, News, Category, Slider, Svyaz, Onas, Tovar, Footer, CartItem, ShippingAddress, \
    Vybor
from .serializers import PremSerializer, HelpSerializer, \
    PublicSerializer, NewsSerializer, CategorySerializer, SliderSerializer, SvyazSerializer, OnasSerializer, \
    PoiskSerializer, TovarSerializer, FooterSerializer, CartItemSerializer, ShippingAddressSerializer, VyborSerializer
import random


class PremApiView(generics.ListAPIView):
    queryset = Prem.objects.all()
    serializer_class = PremSerializer


class OnasApiView(generics.ListAPIView):
    queryset = Onas.objects.all()
    serializer_class = OnasSerializer


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
    serializer_class = PoiskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nametovar']

    # def get_queryset(self, request):
    #     query = request.value
    #
    # queryset = Tovar.objects.filter(nametovaricontains='query', quantitygt=0)
    # if not queryset:
    #     return [Tovar.objects.filter(cat_id=i).order_by('?')[:1] for i in range(1, 6)]
    # else:
    #     return queryset[:12]


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


class CartItemApiView(generics.ListAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get(self, requset, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)

        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def delete(self, request, id=None):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Успешно удалено!"})
from rest_framework.response import Response
from rest_framework import generics, pagination, filters, status
from rest_framework.decorators import api_view

from .models import Prem, Help, Public, News, Category, Slider, Svyaz, Onas, Tovar, Footer, Vybor
from .serializers import PremSerializer, HelpSerializer, \
    PublicSerializer, NewsSerializer, CategorySerializer, SliderSerializer, SvyazSerializer, OnasSerializer, \
    PoiskSerializer, TovarSerializer, FooterSerializer, VyborSerlializer
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

    queryset = Tovar.objects.all()
    serializer_class = PoiskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nametovar']


    # def get_queryset(self):
    #     ret=self.kwargs
    #     print(self.kwargs)
    #     # return Tovar.objects.filter(nametovar=ret)


class FooterApiView(generics.ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer

class VyborApiView(generics.ListAPIView):
    queryset = Vybor.objects.all()
    serializer_class = VyborSerlializer








    # def list_posik(self, request,):
    #     aza = Tovar.objects.all()
    #     Search_aza = PoiskSerializer(aza, many=True).data
    #     return Response({
    #         Search_aza
    #     },
    #         status=status.HTTP_200_OK)




# @api_view(['GET'])
# def SearchApi(request,*args, **daw,):
#     queryset = Tovar.objects.all()
#     serializer_class = PoiskSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['nametovar']
#     print(filter_backends)
#
#     return Response({
#         'Азат':search_fields,
#         'da': queryset
#     },
#         status=status.HTTP_200_OK)


class TovarApiView(generics.ListAPIView):
    queryset = Tovar.objects.all()
    serializer_class = TovarSerializer


class SliderApiView(generics.ListAPIView):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer

# class NovinkiApiView(generics.ListAPIView):
#     queryset = Tovar.objects.filter(newlst=True)
#     serializer_class = NovinkiListSerializer


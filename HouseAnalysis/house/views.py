import json
from django.shortcuts import HttpResponse
from django.views.generic.base import View
from django.db.models import Avg

from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import GenericViewSet

import redis
redis_pool = redis.ConnectionPool(host='127.0.0.1', port=6379, password='', db=4)
redis_conn = redis.Redis(connection_pool=redis_pool)

# 缓存（内存级别）
from rest_framework_extensions.cache.mixins import CacheResponseMixin

from .models import Api, Elevator, Floor, Layout, Region, Decortion, Purposes, Orientation, Constructure
from .serializers import HouseSerializer, ElevatorSerializer, FloorSerializer, LayoutSerializer
from .serializers import RegionSerializer, DecortionSerializer, PurposesSerializer, OrientationSerializer, ConstructureSerializer


# Create your views here.


class HousePagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

import time
class index(View):
    def get(self,request):
        redis_conn.mget(["all_number", "com_number", "mean_price", "mean_unit_price"])
        data = {
            "all_number": all_number,
            "com_number": com_number,
            "mean_price": mean_price,
            "mean_unit_price": mean_unit_price
        }
        res_json = json.dumps(data)
        return HttpResponse(res_json, content_type='application/json')

class HouseListViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Api.objects.all()
    serializer_class = HouseSerializer
    pagination_class = HousePagination
    search_fields = ('title', 'region', 'community_name')
    ordering_fields = ('price', 'unit_price')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ElevaorViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class FloorViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Floor.objects.all()
    serializer_class = FloorSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class LayoutViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Layout.objects.all()
    serializer_class = LayoutSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class RegionViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class DecortionViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Decortion.objects.all()
    serializer_class = DecortionSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PurposesViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Purposes.objects.all()
    serializer_class = PurposesSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class ConstructureViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Constructure.objects.all()
    serializer_class = ConstructureSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class OrientationViewSet(CacheResponseMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Orientation.objects.all()
    serializer_class = OrientationSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

# class Elevator(View):
#     def get(self, request):
#         h = Api.objects.filter(elevator='有')
#         n = Api.objects.filter(elevator='无')
#         has_el_num = h.count()
#         has_mean_price = h.aggregate(Avg('price'))
#         has_mean_unit_price = h.aggregate(Avg('unit_price'))
#         no_el_num = n.count()
#         no_mean_price = n.aggregate(Avg('price'))
#         no_mean_unit_price = n.aggregate(Avg('unit_price'))
#
#         data = {
#             "has_el_num":has_el_num,
#             "no_el_num":no_el_num,
#             "has_mean_price":has_mean_price,
#             "has_mean_unit_price":has_mean_unit_price,
#             "no_mean_price":no_mean_price,
#             "no_mean_unit_price":no_mean_unit_price
#         }
#         res_json = json.dumps(data,sort_keys=True)
#         return HttpResponse(res_json, content_type='application/json')

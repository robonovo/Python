from django.shortcuts import render
from rest_framework import viewsets, filters
from .serializers import StockSerializer, UserSerializer
from .models import Stock
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model


class StockViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filter_fields = ('market_name',)
    ordering = ('stock_gain',)
    search_fields = ('stock_name',)


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

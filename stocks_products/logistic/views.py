from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter, CharFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product, Stock
from .serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', ]
    ordering_fields = ['id', 'title', 'description', ]


class StockFilter(FilterSet):
    products = NumberFilter(field_name='products')
    products__product = NumberFilter(field_name='products')
    # products__product__title = CharFilter(field_name='products__product__title')

    class Meta:
        model = Stock
        fields = ['products', ]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = [DjangoFilterBackend, ]

    #filterset_fields = ('products', 'products__product', 'products__product__title')
    filterset_class = StockFilter

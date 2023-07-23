from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']

    def create(self, validated_data):
        return super().create(validated_data)


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = '__all__'

    def create(self, validated_data):
        positions = validated_data.pop('positions')

        # create stock record
        stock = super().create(validated_data)

        # loop through positions
        for p in positions:
            StockProduct(stock=stock, **p).save()
        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')

        # update stock record
        stock = super().update(instance, validated_data)

        # loop through positions
        for p in positions:
            sp = StockProduct.objects.filter(stock=stock, product=p['product'], price=p['price'])
            if sp:
                sp.update(quantity=p['quantity'])
            else:
                StockProduct.objects.create(stock=stock, **p)

        return stock

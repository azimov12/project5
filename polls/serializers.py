from rest_framework import serializers
from .models import Market, Supermarket

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ("market_name", "market_type")

class SupermarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supermarket
        fields = ("smarket_name", "smarket_type")        
from django.shortcuts import render, get_object_or_404
from .models import Market, Supermarket
from .serializers import MarketSerializer, SupermarketSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class Detail(APIView):
    def get(self, request, *args, **kwargs):
        markets = get_object_or_404(Market, id = kwargs['market_id'])
        result = MarketSerializer(markets)
        return Response(result.data)

class All(APIView):    
    def get(self, request):
        markets = Market.objects.all()
        result = MarketSerializer(markets, many=True)
        
        return Response(result.data)   

class CreateMarketView(APIView):
    def post(self, request):
        user_body = request.data 
        serializer = MarketSerializer(data = user_body)          
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)  

class Detail2(APIView):
    def get(self, request, *args, **kwargs):
        s_markets = get_object_or_404(Supermarket, id = kwargs['supermarket_id'])
        res = SupermarketSerializer(s_markets)
        return Response(res.data)

class All2(APIView):    
    def get(self, request):
        s = Supermarket.objects.all()
        result = SupermarketSerializer(s, many=True)
        
        return Response(result.data)   

class CreateSupermarketView(APIView):
    def post(self, request):
        user_body = request.data 
        serializer = SupermarketSerializer(data = user_body)          
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)          
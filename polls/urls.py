from django.urls import path
from .views import All, Detail, All2, Detail2, CreateMarketView, CreateSupermarketView

urlpatterns = [
    path('detail/<int:market_id>', Detail.as_view()),
    path('all/', All.as_view()),
    path('detail2/<int:supermarket_id>', Detail2.as_view()),
    path('all2/', All2.as_view()),
    path('create1/', CreateMarketView.as_view()),
    path('create2/', CreateSupermarketView.as_view()),
]
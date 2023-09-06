from django.db import models

class Market(models.Model):
    market_name = models.CharField(max_length=25,default='')
    market_type = models.CharField(max_length=25, default='')

    class Meta:
        db_table = 'polls_market'

class Supermarket(models.Model):
    smarket_name = models.CharField(max_length=25,default='')
    smarket_type = models.CharField(max_length=25, default='')        
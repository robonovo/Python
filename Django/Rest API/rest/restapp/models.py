from django.db import models


class Stock(models.Model):
    stock_name = models.CharField(max_length=100)
    stock_price = models.CharField(max_length=100)
    stock_gain = models.CharField(max_length=100)
    market_name = models.CharField(max_length=200)

from django.db import models
from datetime import datetime
from enum import Enum


class DividendType(Enum):
    NONE = "none"
    CASH = "cash"
    SHARES = "shares"
    OTHER = "other"


class BaseModel(models.Model):
    created = models.DateTimeField(default=datetime.utcnow())
    created_by = models.CharField(max_length=32)
    modified = models.DateTimeField(default=datetime.utcnow())
    modified_by = models.CharField(max_length=32)


class Stock(BaseModel):
    """
    A stock is base information about a security
    """

    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=8)
    dividend_type = models.CharField(max_length=8, default=DividendType.NONE)


# class DividendDistributionDates(BaseModel):
#     """
#     For each stock, list dividend distribution dates so we can
#     fetch dividend information.
#     """
#     stock_pk = models.ForeignKey('Stock', on_delete=models.CASCADE)
#     date = models.DateField()

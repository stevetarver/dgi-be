#
# generic views: http://www.django-rest-framework.org/api-guide/generic-views/
#
import json
from rest_framework import generics
from ..models import Stock
from .serializers import StockSerializer


class StockListCreateAPIView(generics.ListCreateAPIView):
    """
    Handle GET list, POST

    Notes:

    * no uniqueness check on url or (url, period)
    """

    serializer_class = StockSerializer
    queryset = Stock.objects.all()


class StockRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handle GET, PUT, DELETE
    """

    serializer_class = StockSerializer
    queryset = Stock.objects.all()

#
# Route table for pages.api
#
from django.urls import path
from .views import StockListCreateAPIView, StockRetrieveUpdateDestroyAPIView


urlpatterns = [
    path("", StockListCreateAPIView.as_view(), name="stocks-list-create"),
    path(
        "<int:pk>",
        StockRetrieveUpdateDestroyAPIView.as_view(),
        name="stocks-read-update-delete",
    ),
]

from django.shortcuts import render
from .models import Stock


def index(request):

    data = Stock.objects.all()
    context = {"title": "Stock List", "stocks": data}
    return render(request, "pages/index.html", context=context)

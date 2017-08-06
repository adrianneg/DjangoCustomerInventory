from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from .models import Item


def index(request):
    items = Item.objects.exclude(amount=0)
    context = {
        "items": items
    }
    return render(request, 'inventory/index.html', context)


def item_detail(request, id):
    try:
        item = Item.objects.get(id=id)
    except Item.DoesNotExist:
        raise Http404("This item does not exist")

    context = {
        "item": item
    }
    return render(request, 'inventory/items_details.html', context)

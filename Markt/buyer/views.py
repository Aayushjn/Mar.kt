from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def display_buyer_dash(request):
    context = {
        'page_name': "Buyer Dashboard",

    }

    return render(request, 'buyer/buyer-dashboard.html', context)


def display_buyer_cat(request: HttpRequest):
    context = {
        'page_name': "Buyer Dashboard",
        'category': "Generic Category",
        'base_bid': 100,
        'high': 300,
    }

    if request.method == "POST":
        context['category'] = request.POST.get(['card-title'])

    return render(request, 'buyer/buyer-category.html', context)


def display_buyer_item(request):
    context = {
        'page_name': "Item Display",
        'category': "Generic Category",
        'item': "Generic Item",
        'base_bid': 100,
        'high': 300,
        'description': "",
        'seller': "Generic Seller",

    }

    return render(request, 'buyer/buyer-item.html', context)

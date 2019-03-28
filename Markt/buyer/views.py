from django.shortcuts import render


# Create your views here.
def display_buyer_dash(request):
    context = {
        'page_name': "Buyer Dashboard",

    }

    return render(request, 'buyer/buyer-dashboard.html', context)


def display_buyer_cat(request):
    context = {
        'page_name': "Buyer Dashboard",
        'category': "Generic Category",
        'base_bid': 100,
        'high': 300,
        'id':9,
    }

    return render(request, 'buyer/buyer-category.html', context)


def display_buyer_item(request,item_id=-1):
    context = {
        'page_name': "Item Display",
        'category': "Generic Category",
        'item': "Generic Item",
        'base_bid': 100,
        'high': 300,
        'description': "",
        'seller': "Generic Seller",
        'id':id,

    }

    return render(request, 'buyer/buyer-item.html', context)

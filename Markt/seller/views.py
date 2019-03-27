from django.shortcuts import render

# Create your views here.

def display_seller_dash(request):
    context = {
        'page_name': "Seller Dashboard",
        'category': "Generic Category",
        'item': "Generic Item",
        'base_bid': 100,
        'high': 300,

    }

    return render(request, 'seller/seller-dashboard.html', context)

def display_seller_list(request):
    context = {
        'page_name': "Seller Listings",
        'category': "Generic Category",
        'base_bid': 100,
        'high': 300,

    }

    return render(request, 'seller/seller-listings.html', context)

def display_seller_item(request):
    context = {
        'page_name': "Item Display",
        'category': "Generic Category",
        'item': "Generic Item",
        'base_bid': 100,
        'high': 300,
        'description': "",
        'seller': "Generic Seller",

    }

    return render(request, 'seller/seller-item.html', context)

def display_seller_mod(request):

    ##### NOTE ###### 
    #basically we run a check to see if a product ID is being passed 
    #if it is, the button value changes to "modify"
    #else it is "add product"
    #Also, if the product ID exists, then the product exists so in the if statement you
    # need to override all these generic context values with the ones in the actual item's object
    # Place them as the default values. 
    # Validation is required in this form 
    context = {
        'page_name': "Item Display",
        'category': "Generic Category",
        'item': "Generic Item",
        'base_bid': 100,
        'high': 300,
        'description': "",
        'seller': "Generic Seller",

    }

    return render(request, 'seller/seller-mod.html', context)

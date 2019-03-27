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
        'base_bid':100,
        'high':300,
    }

    return render(request, 'buyer/buyer-category.html', context)
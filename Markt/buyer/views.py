from django.shortcuts import render

# Create your views here.
def display_buyer_dash(request):
    context = {
        'page_name': "Buyer Dashboard",
        
    }

    return render(request, 'buyer/buyer-dashboard.html', context)

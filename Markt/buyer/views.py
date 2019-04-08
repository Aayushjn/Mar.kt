from django.core.mail import EmailMessage
from django.http import HttpRequest
from django.shortcuts import render

from Markt.settings import EMAIL_HOST_USER
from .models import Product
from seller.models import Bid, Mail
from homepage.models import User


# Create your views here.
def display_buyer_dash(request):
    context = {
        'page_name': "Buyer Dashboard",
        # 'cat_id':9
    }
    return render(request, 'buyer/buyer-dashboard.html', context)


def display_buyer_cat(request, category_id):
    context = {
        'page_name': "Buyer Dashboard",
        'category': "Generic Category",
        # 'base_bid': 100,
        # 'high': 300,
        # 'id':0,

    }

    if category_id == '1':
        context['category'] = 'Textbooks'
    elif category_id == '2':
        context['category'] = 'QPs'
    elif category_id == '3':
        context['category'] = 'Notes'
    elif category_id == '4':
        context['category'] = 'Furniture'

    products = Product.objects.filter(cat_id=int(category_id))
    context['products'] = products

    # if request.method == "POST":
    #     context['category'] = request.POST.get('card-title')

    return render(request, 'buyer/buyer-category.html', context)


def display_buyer_item(request, item_id):
    context = {
        'page_name': "Item Display",
        'category': "Generic Category",
        'cat_id': 9,
        'item': "Generic Item",
        'base_bid': 100,
        'high': 300,
        'description': "",
        'seller': "Generic Seller",
        # 'id':id,

    }

    p = Product.objects.get(id=item_id)
    context['category'] = p.category
    context['cat_id'] = p.cat_id
    context['item'] = p.name
    context['base_bid'] = p.minimum_bid
    context['high'] = p.current_high_bid
    context['description'] = p.description
    context['seller'] = p.vendor_id.name

    if request.method == 'POST':
        context['bid_value'] = request.POST['bid_value']
        try:
            if p.vendor_id == User.objects.get(id=request.session['userid']):
                context['errormessage'] = "Sorry! You cannot bid on your product"
        # passing the bid value to create a mail
        except:
            bid = Bid()
            bid.product_id = p
            bid.buyer_id = User.objects.get(id=request.session['userid'])
            bid.price = float(context['bid_value'])
            bid.save()
            if p.current_high_bid < bid.price:
                p.current_high_bid = bid.price
            p.save()
            return render(request, 'buyer/sample-mail.html', context)

    return render(request, 'buyer/buyer-item.html', context)

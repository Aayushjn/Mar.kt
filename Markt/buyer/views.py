from django.http import HttpRequest
from django.shortcuts import render

from .models import Product
from seller.models import Bid, Mail
from homepage.models import User


# Create your views here.
def display_buyer_dash(request):
    if 'userid' not in request.session.keys() :
        return redirect(reverse('homepage:home'))
    context = {
        'page_name': "Buyer Dashboard",
        # 'cat_id':9
    }
    return render(request, 'buyer/buyer-dashboard.html', context)


def display_buyer_cat(request, category_id):
    if 'userid' not in request.session.keys() :
        return redirect(reverse('homepage:home'))
    context = {
        'page_name': "Buyer Dashboard",
        'category': "Generic Category",
        'cat_id':9,
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
    if 'userid' not in request.session.keys() :
        return redirect(reverse('homepage:home'))
    
    product=Product.objects.get(id=item_id)

    context = {
        'page_name': "Item Display",
        'product':product,
        'cat_id':9,
    }

    if product.vendor_id!=request.session['userid']:
        context['notmyproduct']=True

    if request.method == 'POST':
        context['bid_value'] = request.POST['bid_value']
        user=User.objects.get(id=request.session['userid'])
        bid = Bid()
        bid.product_id = product
        bid.buyer_id = User.objects.get(id=request.session['userid'])
        bid.price = float(context['bid_value'])
        bid.save()
        if product.current_high_bid < bid.price:
            product.current_high_bid = bid.price
        product.save()

        reply=Mail()
        reply.buyer_id=user
        reply.vendor_id=product.vendor_id
        reply.bid_id=bid
        reply.message_type=1
        reply.save()
        context['placed']=True
        return render(request, 'buyer/buyer-item.html', context)

    return render(request, 'buyer/buyer-item.html', context)

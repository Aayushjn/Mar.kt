from django.shortcuts import render, redirect, reverse
from buyer.models import Product
from homepage.models import User
from .models import Bid, Mail


# Create your views here.

def display_seller_dash(request):
    context = {
        'page_name': "Seller Dashboard",
        'category': "Generic Category",
        'item': "Generic Item",
        'base_bid': 100,
        'high': 300,
        'cat_id': 9,

    }

    return render(request, 'seller/seller-dashboard.html', context)


def display_seller_list(request, category_id):
    context = {
        'page_name': "Seller Listings",
        'category': "Generic Category",
        # 'base_bid': 100,
        # 'high': 300,
        # 'id':0,
    }

    items = Product.objects.filter(vendor_id=request.session['userid'])
    context['items'] = items
    return render(request, 'seller/seller-listings.html', context)


def display_seller_item(request, item_id):
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
    return render(request, 'seller/seller-item.html', context)


def display_seller_mod(request):
    ##### NOTE ######
    # basically we run a check to see if a product ID is being passed
    # if it is, the button value changes to "modify"
    # else it is "add product"
    # Also, if the product ID exists, then the product exists so in the if statement you
    # need to override all these generic context values with the ones in the actual item's object
    # Place them as the default values.
    # Validation is required in this form
    context = {
        'page_name': "Item Display",
        'category': "Generic Category",
        'item': "Generic Item",
        'base_bid': 100,
        'high': 300,
        'description': "generic description",
        'seller': "Generic Seller",
        "cat_id": 9,
        "button_text": "Add Product"

    }
    context['seller'] = request.session['username']
    if request.method == 'POST':
        context['category'] = request.POST['category']
        user = User.objects.get(id=request.session['userid'])
        product = Product()
        product.name = request.POST['name']
        product.category = request.POST['category']
        product.vendor_id = user
        product.description = request.POST['description']
        product.minimum_bid = request.POST['base_bid']
        product.current_high_bid = 0
        product.image_link = "https://www.google.com/search?q=question+paper+image&rlz=1C1CHBD_enIN746IN746&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjRoZP21bThAhURwqYKHZT0C8QQ_AUIDigB&biw=1367&bih=633#"
        if product.category == 'Textbooks':
            product.cat_id = 1
        elif product.category == 'QPs':
            product.cat_id = 2
        elif product.category == 'Notes':
            product.cat_id = 3
        elif product.category == 'Furniture':
            product.cat_id = 4
        product.save()
        return redirect(reverse('seller:dashboard'))
    return render(request, 'seller/seller-mod.html', context)

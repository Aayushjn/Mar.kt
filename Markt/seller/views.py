from django.shortcuts import render, redirect, reverse
from buyer.models import Product
from homepage.models import User
from .models import Bid, Mail
import pdb;
# Create your views here.

def display_seller_dash(request):
    if 'userid' not in request.session.keys() :
        return redirect(reverse('homepage:home'))
    context = {
        'page_name': "Seller Dashboard",
        "cat_id":9,
    }
    userid=request.session['userid']
    products=Product.objects.filter(vendor_id=userid).order_by('-current_high_bid')[:3]
    products=list(products)
    while len(products)<3:
        products.append(None)
    if products[0] is not None:
        context['item1']=products[0]
    if products[0] is not None:
        context['item2']=products[1]
    if products[0] is not None:
        context['item3']=products[2]
    

    return render(request, 'seller/seller-dashboard.html', context)


def display_seller_list(request, category_id):
    if 'userid' not in request.session.keys() :
        return redirect(reverse('homepage:home'))
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
    if 'userid' not in request.session.keys() :
        return redirect(reverse('homepage:home'))
    context = {
        'page_name': "Item Display",
        'category': "Generic Category",
        'cat_id': 9,
        'item': "Generic Item",
        'base_bid': 100,
        'high': 300,
        'description': "",
        'seller': "Generic Seller",
        'id':id,
    }
    p = Product.objects.get(id=item_id)
    context['category'] = p.category
    context['cat_id'] = p.cat_id
    context['item'] = p.name
    context['base_bid'] = p.minimum_bid
    context['high'] = p.current_high_bid
    context['description'] = p.description
    context['seller'] = p.vendor_id.name
    context['id'] = p.id


    return render(request, 'seller/seller-item.html', context)


def display_seller_mod(request,item_id):
    ##### NOTE ######
    # basically we run a check to see if a product ID is being passed
    # if it is, the button value changes to "modify"
    # else it is "add product"
    # Also, if the product ID exists, then the product exists so in the if statement you
    # need to override all these generic context values with the ones in the actual item's object
    # Place them as the default values.
    # Validation is required in this form
    if 'userid' not in request.session.keys() :
        return redirect(reverse('homepage:home'))
    context = {
        'page_name': "Item Display",
        'category': "Item category",
        'item': "New Item",
        'base_bid': 0,
        'high': 300,
        'description': "Add a description",
        'seller': request.session['username'],
        "cat_id":9,
        "button_text": "Add Product",
        "delete_button": True
    }

    context['seller'] = request.session['username']

    # to modify a product
    if item_id != "-1":
        p = Product.objects.get(id=item_id)
        context['category'] = p.category
        context['item'] = p.name
        context['base_bid'] = p.minimum_bid
        context['description'] = p.description
        context['button_text'] = "Modify Product"
        if p.category == 'Textbooks':
            context['cat_id'] = 1
        elif p.category == 'QPs':
            context['cat_id'] = 2
        elif p.category == 'Notes':
            context['cat_id'] = 3
        elif p.category == 'Furniture':
            context['cat_id'] = 4

        if 'delete-listing' in request.POST:
            p.delete()
            return redirect(reverse('seller:dashboard'))

        if request.method == 'POST' and context['button_text'] == 'Modify Product':
            p.name = request.POST['name']
            p.category = request.POST['category']
            p.description = request.POST['description']
            p.minimum_bid = request.POST['base_bid']
            if p.category == 'Textbooks':
                p.cat_id = 1
            elif p.category == 'QPs':
                p.cat_id = 2
            elif p.category == 'Notes':
                p.cat_id = 3
            elif p.category == 'Furniture':
                p.cat_id = 4
            p.save()
            return redirect(reverse('seller:dashboard'))
    else:
        context['delete_button'] = False

    if request.method == 'POST' and context['button_text'] == 'Add Product':
        context['category'] = request.POST['category']
        user = User.objects.get(id=request.session['userid'])
        product = Product()
        product.name = request.POST['name']
        product.category = request.POST['category']
        product.vendor_id = user
        product.description = request.POST['description']
        product.minimum_bid = request.POST['base_bid']
        product.current_high_bid = 0
        product.image_link = "https://www.google.com/search?q=question+paper+image&rlz=1C1CHBD_enIN746IN746&source" \
                             "=lnms&tbm=isch&sa=X&ved=0ahUKEwjRoZP21bThAhURwqYKHZT0C8QQ_AUIDigB&biw=1367&bih=633# "
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

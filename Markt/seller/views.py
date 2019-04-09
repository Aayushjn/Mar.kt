from buyer.models import Product
from django.shortcuts import render, redirect, reverse
from homepage.models import User
from seller.models import Bid
from django.core.files.storage import FileSystemStorage
from Markt import settings
import os


# Create your views here.

def display_seller_dash(request):
    if 'userid' not in request.session.keys():
        return redirect(reverse('homepage:home'))
    context = {
        'page_name': "Seller Dashboard",
        "cat_id": 9,
    }
    userid = request.session['userid']
    products = Product.objects.filter(vendor_id=userid).order_by('-current_high_bid')[:3]
    products = list(products)
    while len(products) < 3:
        products.append(None)
    if products[0] is not None:
        context['item1'] = products[0]
    if products[0] is not None:
        context['item2'] = products[1]
    if products[0] is not None:
        context['item3'] = products[2]

    return render(request, 'seller/seller-dashboard.html', context)


def display_seller_list(request, category_id):
    if 'userid' not in request.session.keys():
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
    if 'userid' not in request.session.keys():
        return redirect(reverse('homepage:home'))
    product = Product.objects.get(id=item_id)
    context = {'page_name': "Item Display", 'product': product,
               'bids': list(Bid.objects.filter(product_id=product).order_by('-price'))}

    return render(request, 'seller/seller-item.html', context)


def display_seller_mod(request, item_id):
    if 'userid' not in request.session.keys():
        return redirect(reverse('homepage:home'))

    context = {
        'username': request.session['username']
    }

    # to modify a product
    if item_id != "-1":
        product = Product.objects.get(id=item_id)
        context['product'] = product
        context['delete_button'] = True
        context['button_text'] = "Modify Product"
        context['editprod'] = True
        if product.category == 'Textbooks':
            context['cat_id'] = 1
        elif product.category == 'QPs':
            context['cat_id'] = 2
        elif product.category == 'Notes':
            context['cat_id'] = 3
        elif product.category == 'Furniture':
            context['cat_id'] = 4

        if request.method == "POST" and 'delete-listing' in request.POST:
            product.delete()
            return redirect(reverse('seller:dashboard'))

        if request.method == 'POST' and context['button_text'] == 'Modify Product':
            product.name = request.POST['name']
            product.category = request.POST['category']
            product.description = request.POST['description']
            product.minimum_bid = request.POST['base_bid']
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

    if item_id == '-1':
        context['product'] = Product()
        context['button_text'] = "Add Product"
        context['cat_id'] = 1
        context['newprod'] = True

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
            myfile = request.FILES['filename']
            if myfile is None:
                context['errorm'] = True
                return render(request, 'seller/seller-mod.html', context)

            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            product.image_link = fs.url(filename)
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

        if request.method == 'POST' and "img-submit" in request.POST:
            context['category'] = request.POST['category']
            user = User.objects.get(id=request.session['userid'])
            product = Product()
            product.name = request.POST['name']
            product.category = request.POST['category']
            product.vendor_id = user
            product.description = request.POST['description']
            product.minimum_bid = request.POST['base_bid']
            product.current_high_bid = 0
            myfile = request.FILES['filename']
            if myfile is None:
                context['errorm'] = True
                return render(request, 'seller/seller-mod.html', context)

            fs = FileSystemStorage()

            save_path = os.path.join(settings.MEDIA_ROOT, 'uploads', myfile.name)
            filename = fs.save(save_path, myfile)
            product.image_link = fs.url(filename)
            product.save()
            return redirect(reverse('seller:dashboard'))

    return render(request, 'seller/seller-mod.html', context)

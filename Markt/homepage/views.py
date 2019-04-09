from django.shortcuts import render, redirect, reverse
from urllib import request
from .models import User


def display_home(request):
    # use request.session to pass anything you need between views
    # delete sessions on pages that aren't dashboard pages to force logout
    # used to display variables within frontend

    request.session.flush()
    context = {
        'page_name': "Home",
    }

    return render(request, 'homepage/index.html', context)


def display_login(request):
    request.session.flush()
    if request.method == 'POST':
        context = {}
        email = request.POST['your_name']
        password = request.POST['your_pass']

        try:
            user = User.objects.get(email_id=email)
        except:
            context['errormessage'] = "This user is not registered"
            return render(request, 'homepage/login.html', context)

        if password != user.password:
            context['errormessage'] = "Password doesn't match"

        request.session['username'] = user.name
        request.session['userid'] = user.id
        return redirect(reverse('homepage:dash_home'))

    else:
        context = {
            'page_name': "Login",
        }
        return render(request, 'homepage/login.html', context)


def display_signup(request):
    context = {}
    request.session.flush()
    if request.method == 'POST':
        name = request.POST.get('name')
        email_id = request.POST.get('email')
        password = request.POST.get('pass')
        re_password = request.POST.get('re_pass')

        if password != re_password:
            context['errormessage'] = "Password doesn't match"
            return render(request, 'homepage/registration.html', context)

        try:
            user = User.objects.get(email_id=email_id)
            context['errormessage'] = "Email ID exists"
            return render(request, 'homepage/registration.html', context)
        except:
            user = User()
            user.name = name
            user.email_id = email_id
            user.password = password
            user.save()
            request.session['username'] = user.name
            request.session['userid'] = user.id
            return redirect(reverse('homepage:dash_home'))

    else:
        context = {
            'page_name': "Sign Up",
        }
        return render(request, 'homepage/registration.html', context)


def display_dash_home(request):
    if 'userid' not in request.session.keys() :
        return redirect(reverse('homepage:home'))
    user=User.objects.get(id=request.session['userid'])
    context = {
        'page_name': "Dashboard",
        'user':user,
    }
    if user.share_phone==True:
        context['shph']=True
    

    if request.method=="POST":
        user.name=request.POST['nameupd']
        user.phone_number=request.POST['phupd']
        user.bio=request.POST['bioupd']
        user.share_phone=False
        if len(request.POST.getlist('numshare'))==1:
            user.share_phone=True
        user.save()
        context['updated']=True

    return render(request, 'homepage/dashboard.html', context)


def display_mail_home(request):
    if 'userid' not in request.session.keys() :
        return redirect(reverse('homepage:home'))
    context = {
        'page_name': "Mailbox"
    }

    return render(request, 'homepage/mailbox.html', context)


def display_mail(request):

    if 'userid' not in request.session.keys() :
        return redirect(reverse('homepage:home'))

    context = {
        'page_name': "Mail View",
        'mail_title': "Send Notes Pls",
        'mail_sender': "Spandu",
        'mail_text': "Yo bro send notes",
        'mail_sent': "Now",
    }

    return render(request, 'homepage/mail-view.html', context)

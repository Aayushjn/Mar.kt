from django.shortcuts import render,redirect
from urllib import request

# Create your views here.

def display_home(request):
    # use request.session to pass anything you need between views
    # delete sessions on pages that aren't dashboard pages to force logout  
    
    #request.session.delete()
    
    # used to display variables within frontend
    context={
        'page_name':"Home",
    }

    return render(request,'homepage/index.html',context)


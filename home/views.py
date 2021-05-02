from django.shortcuts import render, HttpResponse
from datetime import datetime
from home import models
from home.models import contact
from django.contrib import messages
# Create your views here.
def index(request):
    context =  {
        'variable':"this is sent"
    }
    # messages.success(request,"this is test message ")
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")
def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is service page")
def menu(request):
    return render(request, 'menu.html')
    # return HttpResponse("this is service page")
def party_hall(request):
    return render(request, 'party hall.html')
    # return HttpResponse("this is service page")
def weddings_order(request):
    return render(request, 'weddings order.html')
    # return HttpResponse("this is service page")

def Contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        print("ho gya kya")
        Email = request.POST.get('Email')
        print("ho gya kya")
        phone = request.POST.get('phone')
        print("ho gya kya")
        suggestion = request.POST.get('suggestion')
        print("ho gya kya")
        Contact = contact(name=name,Email=Email, phone=phone ,suggestion=suggestion, date=datetime.today())
        Contact.save()
        # message display for submission
        messages.success(request, 'Your message has been sent!')
    
          

          
    return render(request, 'contact.html')
    # return HttpResponse("this is contact page")

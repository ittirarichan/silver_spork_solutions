from django.shortcuts import render,redirect
from .models import *



# Create your views here.
def home(req):
    return render(req,'home.html')
    
def contact(req):
    return render(req,'contact.html')

def about(req):
    return render(req,'about.html')


def courses(req):
    # if 'user' in req.session:
    data=Course.objects.all()
    return render (req,'courses.html',{'courses':data})
    # else:
        # return redirect(home)


def contact(req):
    # if 'shop' in req.session:
    if req.method=='POST'():
        name=req.POST['name']
        email=req.POST['email']
        message=req.POST['message']
        data=Contact.objects.create(name=name,email=email,message=message)
        data.save()
        return render (req,'contact.html')
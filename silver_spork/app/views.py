from django.shortcuts import render,redirect
from .models import *



# Create your views here.
def home(req):    
    data=Course.objects.all()[:3]
    return render(req,'home.html',{'courses':data})
    
def contact(req):
    return render(req,'contact.html')

def about(req):
    return render(req,'about.html')


def courses(req):
    data=Course.objects.all()
    return render (req,'courses.html',{'courses':data})


def view_courses(req,c_id):
    data=Course.objects.get(pk=c_id)
    return render(req,'view_courses.html',{'courses':data})


def contact(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        message=req.POST['message']
        data=Contact.objects.create(name=name,email=email,message=message)
        data.save()
        return redirect(contact)
    else:
        return render (req,'contact.html')
    

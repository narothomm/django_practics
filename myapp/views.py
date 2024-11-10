from django.shortcuts import render
from django.http import HttpResponse

def home (request):
   return HttpResponse("This is home page")
  
def out (request):
   return HttpResponse("This is out page")

def details (request):
   return HttpResponse("This is details page.I Include many items of data")

def about(request):
   context={
      "pagetitle":"Wellcome to about page",
      "content":"Here we include html related data.",
      "footer":"2024 my about page"
   }
   return render(request,"about.html",context)

def index(request):
   context={
      "pagetitle":"Wellcome index page",
      "content":"Here we include html1 related data and I inherite from layout.html",
      "footer":"2024 my indext page"  
   }
   return render(request,"index.html",context)

def contact(request):
   email="contact@gmail.com"
   social_profiles=[
      "Facebook:fb.me/example",
      "Twiter:twiter.com/example",
      "Youtube:youtube.com/channellid"
   ]
   hq="d"
   return render(request,"contact.html",{"emailaddress":email,"socialprofiles":social_profiles,"hq":hq})

from django.shortcuts import render

def experiment(request, person=None):
    if person is None:
        person = "guest"
    return render(request, "experiment.html", {"data": person})


def experiment_greet(request,person,greet):
    return render(request,"experiment.html",{"data":person,"geetings":greet}) 
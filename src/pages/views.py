from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# Create a homepage
def home_view(request, *args, **kwargs): # arguments and key arguments
    #return HttpResponse('<h1>Plants, bitch</h1>') # Used HttpResponse to interpret the html STRING.
    return render(request, "home.html",{}) # return a html template rather than using httpresponse

# Create contact page
def contact_view(request, *args, **kwargs):
    #return HttpResponse('<h1>Contact Page</h1>')
    return render(request, "contact.html",{}) 

# Create about page
def about_view(request, *args, **kwargs):
    #return HttpResponse('<h1>About this site</h1> <p1>I love plants</p1>')
    return render(request, "about.html",{}) 
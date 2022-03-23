from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #*args, **kwargs
    #return HttpResponse("<h1>Hello World</h1>") #String of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html",{})

def about_view(request, *args,**kwargs):
    #return HttpResponse("<h1>About page</h1>")
    my_context={
        "my_text":"This is about us",
        "my_number":123,
        "my_list":[123,231,321,"abc"]
    }
    return render(request, "about.html", my_context)
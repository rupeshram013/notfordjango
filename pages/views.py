from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request):

    #return HttpResponse("<h1>HomePage</h1>")
    return render(request, "index.html",{})


def about_view(request):

    return HttpResponse("<h1>AboutPage</h1>")


def contact_view(request):

    return HttpResponse("<h1>ContactPage</h1>")


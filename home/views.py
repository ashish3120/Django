from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    # return HttpResponse("<h1>Ashish is the owner of this Django Server</h1>")
    return render(request,"home/index.html")

def success_page(request):
    print("*" * 10 )
    return HttpResponse("<h1>This is a Success Page</h1>")

def work(request):
    return HttpResponse("<h1>The Page is under Construction</h1>")

def about(request):
    return render(request,"home/about.html")

def contact(request):
    return render(request,"home/contact.html")
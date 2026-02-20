from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    # return HttpResponse("<h1>Ashish is the owner of this Django Server</h1>")
    return render(request,"index.html")

def success_page(request):
    print("*" * 10 )
    return HttpResponse("<h1>This is a Success Page</h1>")

def work(request):
    return HttpResponse("<h1>The Page is under Construction</h1>")
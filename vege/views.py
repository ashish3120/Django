from django.shortcuts import render
from .models import *


# Create your views here.
def recipies(request):
    if request.method == "POST":
        data = request.POST
        recipie_image = request.FILES.get("recipie_image")
        recipie_name = data.get("recipie_name")
        recipie_description = data.get("recipie_description")

        Recipie.objects.create(
            recipie_image=recipie_image,
            recipie_name=recipie_name,
            recipie_description=recipie_description,
        )

    queryset = Recipie.objects.all()
    context = {"recepies": queryset}

    return render(request, "recipies.html", context)

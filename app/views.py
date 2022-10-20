from django.shortcuts import render
# Create your views here.


def homescreen(request):
    return render(request, "base.html")

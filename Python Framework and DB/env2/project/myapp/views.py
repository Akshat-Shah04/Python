from django.shortcuts import render
from django.utils.translation import activate


def hello(request):
    activate("fr")
    return render(request, "hello.html")

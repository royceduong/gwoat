from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'first_app/home.html')
    
def test(request):
    return HttpResponse("Test Page")
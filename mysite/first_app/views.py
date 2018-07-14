from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UploadFileForm

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'first_app/home.html')
    
def process(request):
    if request.method == 'POST':
        # form = DocumentForm(request.POST, request.FILES)
        print(request.FILES)
    return redirect('/')
def test(request):
    return HttpResponse("Test Page")


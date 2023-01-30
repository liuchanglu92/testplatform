from django.shortcuts import render
from django.http import HttpResponse, response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,'home.html')

@csrf_exempt
def page_not_found(request,exception):
    return render(request,'404.html')
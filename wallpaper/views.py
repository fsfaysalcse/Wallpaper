from django.shortcuts import render,HttpResponse
from .models import *

# Create your views here.

def index(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories
    }
    return render(request,'index.html',context)

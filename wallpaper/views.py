from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import *

# Create your views here.

def index_view(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
    }
    return render(request,'index.html',context)

def details_view(request,id):
    category = Category.objects.get(id=id)
    wallpapers = Wallpaper.objects.filter(category_id=category.id)
    context = {
        'wallpapers':wallpapers,
        'name':category.name
    }
    tamplate = 'details.html'
    return render(request,tamplate,context)

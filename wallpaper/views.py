from django.shortcuts import render,HttpResponse,get_object_or_404,resolve_url
from .models import *


import requests
from bs4 import BeautifulSoup


# Create your views here.

def index_view(request):
    categories = Category.objects.all()
    context = {
        'categories' : categories,
    }
    return render(request,'index.html',context)

def details_view(request,id):
    category = Category.objects.get(pk = id)
    wallpapers = Wallpaper.objects.filter(category_id=category.pk)
    context = {
        'wallpapers':wallpapers,
        'name':category.name
    }
    tamplate = 'details.html'
    return render(request,tamplate,context)



def saveDataOp(title,image):
    wall = Wallpaper.objects.create(
        title=title,decs=title,wallpaper_file=image,category=Category.objects.get(id=6)
    )
    wall.save()

def scrapingOp(title, image):
    page = requests.get(image)
    soup = BeautifulSoup(page.text, 'html.parser')
    wall_div = soup.find(class_='sc-jTzLTM jOnymC')
    img_url = wall_div.find('img').get('src')
    saveDataOp(title,img_url)

def insert_view(request):
    page = requests.get('https://www.zedge.net/find/wallpapers/travel')
    soup = BeautifulSoup(page.text, 'html.parser')
    wall_div = soup.find_all(class_='sc-gxMtzJ kfpCqg')

    for wallpaper in wall_div:
        walli = wallpaper.find('a')
        title = walli.contents[0]
        image = 'https://www.zedge.net' + walli.get('href')
        scrapingOp(title, image)

    return HttpResponse("Hello World")















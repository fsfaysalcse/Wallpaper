from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=15, null=True, default=None)
    category_thumb = models.ImageField(upload_to='images/category', null=True, default=None)
    crated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=20,null=True,default=None)

    def __str__(self):
        return self.name


class Wallpaper(models.Model):
    title = models.CharField(max_length=50,null=True,default=None)
    decs = models.CharField(max_length=500,null=True,default=None)
    wallpaper_file = models.ImageField(upload_to='images/wallpapers')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    upload_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



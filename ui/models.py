from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=75)
    slug=models.SlugField()

    def __str__(self):
        return self.name
class SubCategory(models.Model):
    name=models.CharField(max_length=75)
    category=models.ForeignKey(Category,default='', on_delete=models.CASCADE)
    slug=models.SlugField()

    def __str__(self):
        return self.name
    
class SubSubCategory(models.Model):
    name=models.CharField(max_length=75)
    subcategory=models.ForeignKey(SubCategory,default='', on_delete=models.CASCADE)
    slug=models.SlugField()

    def __str__(self):
        return self.name
    

class Model(models.Model):
    name=models.CharField(max_length=75)
    slug=models.SlugField()

    def __str__(self):
        return self.name
    

class Brand(models.Model):
    name=models.CharField(max_length=75)
    slug=models.SlugField()

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name=models.CharField(max_length=75)
    price=models.IntegerField()
    model=models.ForeignKey(Model,default='', on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand, default='', on_delete=models.CASCADE)
    subsubcategory=models.ForeignKey(SubSubCategory,default='', on_delete=models.CASCADE)
    description=models.TextField()
    image=models.ImageField(blank=True)
    shippingFrom=models.CharField()
    availability=models.CharField()
    condition=models.CharField()
    views = models.PositiveIntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    slug=models.SlugField()


    def __str__(self):
        return self.name
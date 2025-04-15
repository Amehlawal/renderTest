from django.contrib import admin
from .models import Product, Model, Brand, Category, SubCategory, SubSubCategory
# Register your models here.
admin.site.register(Product)
admin.site.register(Model)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(SubSubCategory)
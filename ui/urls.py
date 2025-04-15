from django.urls import path
from . import views

app_name = "ui"

urlpatterns = [
    path('', views.homepage, name='home'),
    path('equipments/', views.equipments, name='equipments'),
    path('search/', views.search, name='search'),
    path('models/', views.models, name='models'),
    path('<slug:slug>/', views.product_page, name="product"),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    
]
from django.urls import path,include
from . import views

#from django.urls import path
from product.views import product_detaills
app_name = 'home'
urlpatterns = [
    path('', views.home,name='homeho'),
    path('product/<int:id>', views.home2, name='home'),
]

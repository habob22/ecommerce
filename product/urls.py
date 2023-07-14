
from django.urls import path,include
from . import views
app_name = 'product'
urlpatterns = [
    path('', views.product_list,name='products'),
    path('<int:id>', views.product_detaills, name='product_detaills',),
]

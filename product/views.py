from django.shortcuts import render
from .models import Product
# Create your views here.

def product_list(request):
    product_list=Product.objects.all()
    context={'product_list':product_list}
    return render(request , 'Product/product_list.html' , context)


def product_detaills(request,id):
    product_detaills=Product.objects.get(id=id)
    context={'product_detaills':product_detaills}
    return render(request , 'Product/product_detaills.html' , context)

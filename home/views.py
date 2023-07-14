from django.shortcuts import render
from product.models import Product
from product.models import FuturProduct
# Create your views here.


def home(request ):
   
    newproduct=Product.objects.all()
    futurproduct=FuturProduct.objects.all()
    context={'newproduct':newproduct,'futurproduct':futurproduct}
    return render(request , 'home/product_list_new.html' , context)
def home2(request ,id):
    nowproduct=Product.objects.get(id=id)
    context={'nowproduct':nowproduct}
    return render(request , 'Product/product_detaills.html' , context)
    
    
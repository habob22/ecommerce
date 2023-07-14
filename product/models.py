from django.db import models


new_type=(
    ('new','new'),
)
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100 )
    category = models.ForeignKey('Category' , on_delete=models.CASCADE )
    desc = models.TextField()
    image = models.ImageField(upload_to='prodcut/' ,  blank=True, null=True)
    prix = models.DecimalField(max_digits=5  , decimal_places=2 )
    discountPrice = models.DecimalField(max_digits=5  , decimal_places=2 )    
    created = models.DateTimeField(auto_now=True)
    size=models.IntegerField()
    new=models.CharField(max_length=10,choices=new_type)
    
    
    def __str__(self) :
        return self.name

class Category(models.Model):
    CATName = models.CharField(max_length=50 )
    CATParent = models.ForeignKey('self' ,limit_choices_to={'CATParent__isnull' : True}, on_delete=models.CASCADE , blank=True, null=True)
    CATDesc = models.TextField( )
    CATImg = models.ImageField(upload_to='category/')    
    
    
    
    
    def __str__(self) :
        return self.CATName
    

class FuturProduct(models.Model):
    name = models.CharField(max_length=100 )
    category = models.CharField(max_length=30)
    desc = models.TextField()
    image = models.ImageField(upload_to='futurprodcut/' ,  blank=True, null=True)
    prix = models.DecimalField(max_digits=5  , decimal_places=2 )   
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.name
    
    
from django.db import models 
from .categorie import categorie


class Product(models.Model):
    name = models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    categorie = models.ForeignKey(categorie,on_delete=models.CASCADE,default=1)
    des=models.CharField(max_length=200,default='')
    image=models.ImageField(upload_to='static/dist/')

    @staticmethod
    def get_all_products_by_category_id(categorie_Id):
        if categorie_Id:
           return Product.objects.filter(categorie=categorie_Id)
        else:
           return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)
   

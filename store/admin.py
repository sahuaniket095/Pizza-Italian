from django.contrib import admin
from .models.product import Product
from .models.categorie import categorie
from .models.customer import customer
from .models.orders import order
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display=['name','price','categorie']

class AdminCategorie(admin.ModelAdmin):
    list_display=['name']

class AdminCustomer(admin.ModelAdmin):
    list_display=['full_name','phone','email','password']



admin.site.register(customer,AdminCustomer)
admin.site.register(Product,AdminProduct)
admin.site.register(categorie,AdminCategorie)
admin.site.register(order)
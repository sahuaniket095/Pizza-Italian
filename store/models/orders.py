from django.db import models
from .product import Product
from .customer import customer
import datetime
class order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    price=models.IntegerField()
    phone=models.CharField(max_length=50,default='',blank=True)
    address=models.CharField(max_length=500,default='',blank=True)
    date=models.DateField(default=datetime.datetime.today)
    status=models.BooleanField(default=False)

    def placeorder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return order .objects.filter(customer=customer_id)   
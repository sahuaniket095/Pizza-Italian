from django.db import models

        
class customer(models.Model):
    full_name= models.CharField(max_length=100)
    phone=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=500)

   
    @staticmethod
    def get_customer_by_email(email):
       try:
           return customer.objects.get(email=email)
       except:
           return False
       
    def isExist(self):
        if customer.objects.filter(email=self.email):
            return True   
        return False
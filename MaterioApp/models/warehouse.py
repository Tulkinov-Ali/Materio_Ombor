from django.db import models
from .auth import User

class WareHose(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    workers = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return f"{self.name} {self.location}"
    
    
    def format_workers(self):
        return{
            "id":self.id,
            "name":self.name,
            "location":self.location,
            "workers":self.workers
        }
    
    
class Product(models.Model):
    name = models.CharField(max_length=250)
    size = models.CharField(max_length=50)
    count = models.CharField(max_length=50)
    price_type = models.CharField(max_length=15)

    
    def __str__(self) -> str:
        return f"{self.name} "
    
    
class Orders(models.Model):
    product = models.ForeignKey(Product,models.CASCADE)
    name = models.CharField(max_length=250)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    count = models.CharField(max_length=50)
    create_data = models.DateTimeField(auto_now_add=True)
    acceptance = models.DateTimeField(auto_now_add=True)
    


class Korzinka(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    quent = models.IntegerField(default=1)
    price = models.BigIntegerField(default=8)
    price_type = models.CharField(max_length=15)
    
    
    def save(self,*args, **kwargs):
        # self.price = int(self.product.selling price) * self.quent
        self.price_type = self.product.price_type
         
        return super(Korzinka,self).save(*args, **kwargs)
       
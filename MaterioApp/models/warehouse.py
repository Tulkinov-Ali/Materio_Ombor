from django.db import models


class WareHose(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    
    def __str__(self) -> str:
        return f"{self.name} {self.location}"
    
    
class Product(models.Model):
    name = models.CharField(max_length=250)
    color = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    count = models.CharField(max_length=50)
    
    

from django.contrib import admin
from .models.auth import User
from .models.warehouse import WareHose,Product,Orders
# Register your models here.

admin.site.register(User)
admin.site.register(WareHose)
admin.site.register(Product)
admin.site.register(Orders)


from django.contrib import admin
from KrishiSahayak.models import CustomerOrder, FoodOrder, Login, SignUp, ShopUpload, FarmerUpload, CustomerOrder

# Register your models here.
admin.site.register(SignUp)
admin.site.register(Login)
admin.site.register(FoodOrder)
admin.site.register(ShopUpload)
admin.site.register(FarmerUpload)
admin.site.register(CustomerOrder)

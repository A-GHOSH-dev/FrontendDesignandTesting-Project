from django.contrib import admin
from KrishiSahayak.models import FoodOrder, Login, SignUp, ShopUpload

# Register your models here.
admin.site.register(SignUp)
admin.site.register(Login)
admin.site.register(FoodOrder)
admin.site.register(ShopUpload)

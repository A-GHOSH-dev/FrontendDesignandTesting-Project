from django.db import models
import os
from twilio.rest import Client

# Create your models here.
#signup
class SignUp(models.Model):
    Sfirstname = models.CharField(max_length=50)
    Slastname = models.CharField(max_length=50)  
    Scountry = models.CharField(max_length=50)
    Sstate = models.CharField(max_length=50)
    Scity = models.CharField(max_length=50)
    Saddress = models.CharField(max_length=300)
    Spin = models.CharField(max_length=30)
    Sphone = models.CharField(max_length=10)
    
    def __str__(self):
        return self.Sfirstname + ' ' + self.Slastname + ' ' + self.Sstate


#login
class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=15)  
   
    
    def __str__(self):
        return self.username + ' ' + self.password



#foodsorder
class FoodOrder(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)  
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    pin = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    productname = models.CharField(max_length=50)
    productID = models.CharField(max_length=20) 
    quantity = models.PositiveIntegerField()
    msg = models.CharField(max_length=500)
    
    def __str__(self):
        return self.firstname + ' ' + self.lastname + ' ' + self.productID


'''def save(self, *args, **kwargs):
        if int(self.quantity) > 0:
            account_sid = 'AC9afeae960cdf883927ff6753fb07896e'
            auth_token = '2fe728095c92dfda06c823b1602bb177'
            client = Client(account_sid, auth_token)

            message = client.messages \
                    .create(
                        body=f'New Order: FirstName:{self.firstname}, LastName:{self.lastname}, ID:{self.productID}, Country:{self.country},state:{self.state},city:{self.city},address:{self.address},pin:{self.pin},phoneno.:{self.phone},productname:{self.productname},quantity:{self.quantity},message:{self.msg}',
                        from_='+15102300421',
                        to='+919163036951'
                    )

            print(message.sid)

            return super().save(*args, **kwargs)

'''


#shopupload
class ShopUpload(models.Model):
    shopproductname = models.CharField(max_length=50)
    IDproduct = models.CharField(max_length=20)  
    price = models.CharField(max_length=10)
    desc = models.CharField(max_length=500)
    shopkeepername = models.CharField(max_length=50)
    shopname = models.CharField(max_length=50)
    shoplocation = models.CharField(max_length=100)
    shopcontact = models.CharField(max_length=10)
    postdate = models.DateTimeField()
#productpic = models.ImageField(upload_to='shops/imagess')
    
    
    def __str__(self):
        return self.shopproductname + ' ' + self.IDproduct + ' ' + self.shopname



#farmerupload
class FarmerUpload(models.Model):
    farmerproducttype = models.CharField(max_length=50)
    farmerproductname = models.CharField(max_length=50)
    IDproductfarmer = models.CharField(max_length=20)  
    pricefarmer = models.CharField(max_length=10)
    descfarmer = models.CharField(max_length=500)
    
    farmername = models.CharField(max_length=50)
    farmerlocation = models.CharField(max_length=100)
    farmercontact = models.CharField(max_length=10)
    postdatefarmer = models.DateTimeField()
    
    
    
    def __str__(self):
        return self.farmerproducttype + ' ' + self.farmerproductname + ' ' + self.IDproductfarmer + ' ' + self.farmername






#customerorder
class CustomerOrder(models.Model):
    Cfirstname = models.CharField(max_length=50)
    Clastname = models.CharField(max_length=50)  
    Ccountry = models.CharField(max_length=50)
    Cstate = models.CharField(max_length=50)
    Ccity = models.CharField(max_length=50)
    Caddress = models.CharField(max_length=300)
    Cpin = models.CharField(max_length=30)
    Cphone = models.CharField(max_length=10)
    Cproductname = models.CharField(max_length=50)
    CproductID = models.CharField(max_length=20) 
    Cquantity = models.PositiveIntegerField()
    Cmsg = models.CharField(max_length=500)
    
    def __str__(self):
        return self.Cfirstname + ' ' + self.Clastname + ' ' + self.CproductID


''' def save(self, *args, **kwargs):
        if int(self.quantity) > 0:
            account_sid = 'AC9afeae960cdf883927ff6753fb07896e'
            auth_token = '2fe728095c92dfda06c823b1602bb177'
            client = Client(account_sid, auth_token)

            message = client.messages \
                    .create(
                        body=f'New Order: FirstName:{self.Cfirstname}, LastName:{self.Clastname}, ID:{self.CproductID}, Country:{self.Ccountry},state:{self.Cstate},city:{self.Ccity},address:{self.Caddress},pin:{self.Cpin},phoneno.:{self.Cphone},productname:{self.Cproductname},quantity:{self.Cquantity},message:{self.Cmsg}',
                        from_='+15102300421',
                        to='+919163036951'
                    )

            print(message.sid)

            return super().save(*args, **kwargs)
'''

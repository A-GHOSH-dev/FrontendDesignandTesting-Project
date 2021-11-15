from KrishiSahayakWeb.settings import RAZORPAY_API_KEY
from django.shortcuts import render, HttpResponse, redirect
from KrishiSahayak.models import SignUp, Login, FoodOrder, ShopUpload, FarmerUpload, CustomerOrder
import razorpay
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.auth import login as auth_login

# Create your views here.
def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')

def home(request):
    #return HttpResponse("This is my home page")
    return render(request, 'home.html')


###################################
#user sign up
###################################

'''def signup(request):
    
    if request.method=="POST":
        Sfirstname=request.POST['Sfirstname']
        Slastname=request.POST['Slastname']        
        Scountry=request.POST['Scountry']
        Sstate=request.POST['Sstate']
        Scity=request.POST['Scity']
        Saddress=request.POST['Saddress']
        Spin=request.POST['Spin']
        Sphone=request.POST['Sphone']
       
        

        print(Sfirstname, Slastname, Scountry, Sstate, Scity, Saddress, Spin, Sphone)

        ins = SignUp(Sfirstname=Sfirstname, Slastname=Slastname, Scountry=Scountry, Sstate=Sstate, Scity=Scity, Saddress=Saddress, Spin=Spin, Sphone=Sphone)  

        ins.save()
        print("Data stored in Sdb")

    #return HttpResponse("This is my home page")
    return render(request, 'signup.html')

'''




def handleSignup(request):
    if request.method=='GET':
        return render(request, 'signup.html')
    if request.method=='POST':
        #Get parameters posted
        username=request.POST['username']
        email=request.POST['email']
        Sfirstname=request.POST['Sfirstname']
        Slastname=request.POST['Slastname']        
        Scountry=request.POST['Scountry']
        Sstate=request.POST['Sstate']
        Scity=request.POST['Scity']
        Saddress=request.POST['Saddress']
        Spin=request.POST['Spin']
        Sphone=request.POST['Sphone']
        pass1=request.POST['pass1']
        pass2=request.POST['pass1']

#    ''' #Check info eerors
#        if len(username)<10:
#            messages.error(request, " Your user name must be under 10 characters")
#            return redirect('signup')
#
#        if not username.isalnum():
#            messages.error(request, " User name should only contain letters and numbers")
#            return redirect('signup')
#        if (pass1!= pass2):
#             messages.error(request, " Passwords do not match")
#             return redirect('signup')'''

        #Create User
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name=Sfirstname
        myuser.Last_name=Slastname
        myuser.save()
        messages.success(request, "Your account has been successfully created")

    
        return redirect('/')


#########################################
#login user
#########################################



#'''
#def login(request):

#    if request.method=="POST":
#        username=request.POST['username'] 
#        password=request.POST['password']
#        
#
#        print(username, password)
#
#        ins = Login(username=username, password=password)  
#
#        ins.save()
#        print("Data stored in Ldb")
#
#    #return HttpResponse("This is my home page")
#    return render(request, 'login.html')
#
#'''

def handleLogin(request):
    if request.method=='GET':
        return render(request, 'login.html')
        
    if request.method=='POST':
        loginusername=request.POST['loginusername'] 
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('handleLogin')
    
    
    #return HttpResponse('handleLogin')

def handleLogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')




def FarmersCorner(request):
    
    #return HttpResponse("This is my home page")
    return render(request, 'FarmersCorner.html')

def payment(request):
    client = razorpay.Client(auth=("rzp_test_9iRXgZk4KS1HrA", "L878VCH8PgBLCStuctIBCdJG"))

    order_amount = 50000
    order_currency = 'INR'
    

    payment_order=client.order.create(dict(amount=order_amount, currency=order_currency, payment_capture=1))
    payment_order_id=payment_order['id']
    #return HttpResponse("This is my home page")
    context={
        'amount':500, 'api_key':RAZORPAY_API_KEY, 'order_id':payment_order_id
    }
    return render(request, 'payment.html', context)

def Agriculture(request):
    #return HttpResponse("This is my home page")
    return render(request, 'Agriculture.html')

def foods(request):
    productcart = ShopUpload.objects.all()
    
    return render(request,"foods.html",{"productcart":productcart})


   

def foodsordernow(request):
    farmerbuyorder = FoodOrder.objects.all()
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']        
        
        country=request.POST['country']
        state=request.POST['state']
        city=request.POST['city']
        address=request.POST['address']
        pin=request.POST['pin']
        phone=request.POST['phone'] 
        
        productname=request.POST['productname']
        productID=request.POST['productID']
        quantity=request.POST['quantity']
        msg=request.POST['msg']
        

        #print(firstname, lastname, country, state, city, address, pin, phone, productname, productID, quantity, msg)

        farmerbuydata = FoodOrder(firstname=firstname, lastname=lastname, country=country, state=state, city=city, address=address, pin=pin, phone=phone, productname=productname, productID=productID, quantity=quantity, msg=msg)  

        farmerbuydata.save()
        return redirect('payment')
        #return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})
        
        
    return render(request,"foodsordernow.html",{"Orders":farmerbuyorder})

    

def shopkeepers(request):
    #return HttpResponse("This is my home page")
    return render(request, 'shopkeepers.html')

def shopupload(request):
    if request.method=="POST":
        shopproductname=request.POST['shopproductname']
        IDproduct=request.POST['IDproduct']        
        
        price=request.POST['price']
        desc=request.POST['desc']
        shopkeepername=request.POST['shopkeepername']
        shopname=request.POST['shopname']
        shoplocation=request.POST['shoplocation']
        shopcontact=request.POST['shopcontact'] 
        
        postdate=request.POST['postdate']
       # productpic=request.POST['productpic']
        


        print(shopproductname, IDproduct, price, desc, shopkeepername, shopname, shoplocation, shopcontact, postdate)

        ins = ShopUpload(shopproductname=shopproductname, IDproduct=IDproduct, price=price, desc=desc, shopkeepername=shopkeepername, shopname=shopname, shoplocation=shoplocation, shopcontact=shopcontact, postdate=postdate)  

        ins.save()
        print("Data stored in SUdb")

    #return HttpResponse("This is my home page")
    return render(request, 'shopupload.html')

def shopview(request):
    farmerbuyorder = FoodOrder.objects.all()
    
    return render(request,"shopview.html",{"farmerbuyorder":farmerbuyorder})
        

def Apiculture(request):
    #return HttpResponse("This is my home page")
    return render(request, 'Apiculture.html')
def Aquaculture(request):
    #return HttpResponse("This is my home page")
    return render(request, 'Aquaculture.html')
def Livestock(request):
    #return HttpResponse("This is my home page")
    return render(request, 'Livestock.html')
def LoremIpsumAgroLtd(request):
    #return HttpResponse("This is my home page")
    return render(request, 'LoremIpsumAgroLtd.html')
def shopkeepers(request):
    #return HttpResponse("This is my home page")
    return render(request, 'shopkeepers.html')
def news(request):
    #return HttpResponse("This is my home page")
    return render(request, 'news.html')
def StreeKrishiMitraNGO(request):
    #return HttpResponse("This is my home page")
    return render(request, 'StreeKrishiMitraNGO.html')
def chatbot(request):
    #return HttpResponse("This is my home page")
    return render(request, 'chatbot.html') 
def NGOCorporate(request):
    #return HttpResponse("This is my home page")
    return render(request, 'NGOCorporate.html') 




def farmerupload(request):
    if request.method=="POST":
        farmerproducttype=request.POST['farmerproducttype']
        farmerproductname=request.POST['farmerproductname']
        IDproductfarmer=request.POST['IDproductfarmer']        
        
        pricefarmer=request.POST['pricefarmer']
        descfarmer=request.POST['descfarmer']
        
        farmername=request.POST['farmername']
        farmerlocation=request.POST['farmerlocation']
        farmercontact=request.POST['farmercontact'] 
        
        postdatefarmer=request.POST['postdatefarmer']
        
        


        print(farmerproducttype, farmerproductname, IDproductfarmer, pricefarmer, descfarmer, farmername, farmerlocation, farmercontact, postdatefarmer)

        ins = FarmerUpload(farmerproducttype=farmerproducttype, farmerproductname=farmerproductname, IDproductfarmer=IDproductfarmer, pricefarmer=pricefarmer, descfarmer=descfarmer, farmername=farmername, farmerlocation=farmerlocation, farmercontact=farmercontact, postdatefarmer=postdatefarmer)  

        ins.save()
        print("Data stored in FUdb")

    #return HttpResponse("This is my home page")
    return render(request, 'farmerupload.html')
    


def CustomerCorner(request):
    customerproductcart = FarmerUpload.objects.all()
    
    return render(request,"CustomerCorner.html",{"customerproductcart":customerproductcart})




def customerorder(request):
    customerbuyorder = CustomerOrder.objects.all()
    if request.method=="POST":
        Cfirstname=request.POST['Cfirstname']
        Clastname=request.POST['Clastname']        
        
        Ccountry=request.POST['Ccountry']
        Cstate=request.POST['Cstate']
        Ccity=request.POST['Ccity']
        Caddress=request.POST['Caddress']
        Cpin=request.POST['Cpin']
        Cphone=request.POST['Cphone'] 
        
        Cproductname=request.POST['Cproductname']
        CproductID=request.POST['CproductID']
        Cquantity=request.POST['Cquantity']
        Cmsg=request.POST['Cmsg']
        

        #print(firstname, lastname, country, state, city, address, pin, phone, productname, productID, quantity, msg)

        customerbuydata = CustomerOrder(Cfirstname=Cfirstname, Clastname=Clastname, Ccountry=Ccountry, Cstate=Cstate, Ccity=Ccity, Caddress=Caddress, Cpin=Cpin, Cphone=Cphone, Cproductname=Cproductname, CproductID=CproductID, Cquantity=Cquantity, Cmsg=Cmsg)  

        customerbuydata.save()
        return redirect('payment')
        #return render(request,"customerorder.html",{"Orders":customerbuyorder})
        
        
    return render(request,"customerorder.html",{"Orders":customerbuyorder})


def viewcustomerorders(request):
    customerbuyorder = CustomerOrder.objects.all()
    
    return render(request,"viewcustomerorders.html",{"customerbuyorder":customerbuyorder})  

















from KrishiSahayakWeb.settings import RAZORPAY_API_KEY
from django.shortcuts import render, HttpResponse
from KrishiSahayak.models import SignUp, Login, FoodOrder, ShopUpload
import razorpay

# Create your views here.
def index(request):
    #return HttpResponse("This is my home page")
    return render(request, 'index.html')

def home(request):
    #return HttpResponse("This is my home page")
    return render(request, 'home.html')

def signup(request):
    
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

def login(request):

    if request.method=="POST":
        username=request.POST['username'] 
        password=request.POST['password']
        

        print(username, password)

        ins = Login(username=username, password=password)  

        ins.save()
        print("Data stored in Ldb")

    #return HttpResponse("This is my home page")
    return render(request, 'login.html')

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
        res = "Dear {} Thanks for your feedback".format(firstname)
        return render(request,"foodsordernow.html",{"status":res,"Orders":farmerbuyorder})
        
        
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
        productpic=request.POST['productpic']
        


        print(shopproductname, IDproduct, price, desc, shopkeepername, shopname, shoplocation, shopcontact, postdate, productpic)

        ins = ShopUpload(shopproductname=shopproductname, IDproduct=IDproduct, price=price, desc=desc, shopkeepername=shopkeepername, shopname=shopname, shoplocation=shoplocation, shopcontact=shopcontact, postdate=postdate, productpic=productpic)  

        ins.save()
        print("Data stored in SUdb")

    #return HttpResponse("This is my home page")
    return render(request, 'shopupload.html')

def shopview(request):
    farmerbuyorder = FoodOrder.objects.all()
    
    return render(request,"shopview.html",{"farmerbuyorder":farmerbuyorder})
        
def CustomerCorner(request):
    #return HttpResponse("This is my home page")
    return render(request, 'CustomerCorner.html')
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
    



















from django.contrib import admin
from django.urls import path, include
from KrishiSahayak import views

admin.site.site_header ="Developer Ananya Ghosh"
admin.site.site_title= "Welcome to my dashboard"
admin.site.index_title="Welcome to my portal"

urlpatterns = [
    
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
   # path('signup', views.signup, name='signup'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('FarmersCorner', views.FarmersCorner, name='FarmersCorner'),
    path('Agriculture', views.Agriculture, name='Agriculture'),
    path('foods', views.foods, name='foods'),
    path('foodsordernow', views.foodsordernow, name='foodsordernow'),
    path('shopkeepers', views.shopkeepers, name='shopkeepers'),
    path('shopupload', views.shopupload, name='shopupload'),
    path('farmerupload', views.farmerupload, name='farmerupload'),
    path('customerorder', views.customerorder, name='customerorder'),
    path('shopview', views.shopview, name='shopview'),
    path('CustomerCorner', views.CustomerCorner, name='CustomerCorner'),
    path('Apiculture', views.Apiculture, name='Apiculture'),
    path('Aquaculture', views.Aquaculture, name='Aquaculture'),
    path('Livestock', views.Livestock, name='Livestock'),
    path('LoremIpsumAgroLtd', views.LoremIpsumAgroLtd, name='LoremIpsumAgroLtd'),
    path('news', views.news, name='news'),
    path('StreeKrishiMitraNGO', views.StreeKrishiMitraNGO, name='StreeKrishiMitraNGO'),
    path('chatbot', views.chatbot, name='chatbot'),
    path('NGOCorporate', views.NGOCorporate, name='NGOCorporate'),
    path('viewcustomerorders', views.viewcustomerorders, name='viewcustomerorders'),
    path('payment', views.payment, name='payment')




    


    
]


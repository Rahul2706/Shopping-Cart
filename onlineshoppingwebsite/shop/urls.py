#from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.index, name="Shop Home"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUS"),
    path('tracker/', views.tracker, name="TrackingStatus"),
    path('search/', views.search, name="Search"),
    path('product/<int:myid>', views.prodView, name="ProductView"),
    path('checkout/', views.checkout, name="CheckOut"),
    path('login/', views.login, name='Login'),
    path('logout/', views.logout_request, name='Logout'),
    path('product/',views.productlist, name='ProductItems'),
    path('handlerequest/',views.handlerequest, name='HandleRequest'),

]

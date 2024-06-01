from django.contrib import admin
from django.urls import path
from store import views
from .views import categories
from .views import cart
from .views import checkout
from .views import orderview
from .middleware.auth import auth_middleware
from .views import pizza,nonvegpizza,cheesepizza,pepperonipizza,margheritapizza,supremepizza,sides
urlpatterns = [
    path('',views.Home,name='Home'),
    path('Home',views.Home,name='Home'),
    path('categories',categories.as_view(),name='categories'), 
    path('pizza',pizza.as_view(),name='pizza'),
    path('nonvegpizza',nonvegpizza.as_view(),name='nonvegpizza'),
    path('cheesepizza',cheesepizza.as_view(),name='cheesepizza'),
    path('pepperonipizza',pepperonipizza.as_view(),name='pepperonipizza'),   
    path('margheritapizza',margheritapizza.as_view(),name='margheritapizza'),
    path('supremepizza',supremepizza.as_view(),name='supremepizza'),   
    path('sides',sides.as_view(),name='sides'),
    path('login',views.login,name='Login'),
    path('logout',views.logout,name='Logout'),
    path('signin',views.signin,name='Signin'),
    path('cart',auth_middleware(cart.as_view()),name='cart'),
    path('checkout',auth_middleware(checkout.as_view()),name='checkout'),
    path('check',views.check,name='check'),
    path('orders',auth_middleware(orderview.as_view()),name='orderview'),
]
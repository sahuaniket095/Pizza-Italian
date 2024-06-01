from django.shortcuts import render,redirect
from .models import Product
from .models import categorie
from .models import customer
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password,make_password
from django.views import View
from .models import order

# Create your views here.

def Home(request):     
        return render(request,'Home.html')

def veggie(request):  
    
    products = Product.objects.filter(categorie_id=2)
    return  render(request,'pizza.html',{'products':products})

def sides(request):
    products = Product.objects.filter(categorie_id=7)
    return  render(request,'pizza.html',{'products':products})
    

def nonvegpizza(request):
    products = Product.objects.filter(categorie_id=3)
    return  render(request,'pizza.html',{'products':products})

def cheesepizza(request):
     products = Product.objects.filter(categorie_id=4)
     return  render(request,'pizza.html',{'products':products})

def supremepizza(request):
     products = Product.objects.filter(categorie_id=6)
     return  render(request,'pizza.html',{'products':products})

def margheritapizza(request):
    products = Product.objects.filter(categorie_id=5)
    return  render(request,'pizza.html',{'products':products})

def pepperonipizza(request):
    products = Product.objects.filter(categorie_id=1)
    return  render(request,'pizza.html',{'products':products})


class orderview(View):
       
       def get(self,request):
              customer=request.session.get('Customer')
              orders=order.get_orders_by_customer(customer)
              print(orders)
              return render(request,'orders.html',{'orders':orders})



class cart(View):
    def get(self,request):    
        ids=list(request.session.get('cart').keys())
        products=Product.get_products_by_id(ids)
        
        return render(request,'cart.html',{'products':products})

class checkout(View):
       def post(self,request):
              address=request.POST.get('address')
              phone=request.POST.get('Phone')
              Customer=request.session.get('Customer')
              cart=request.session.get('cart')
              product=Product.get_products_by_id(list(cart.keys()))
              print(address,phone,customer,product)
              for i in product:
                     Order=order(customer=customer(id=Customer),
                                 product=i,
                                 price=i.price,
                                 address=address,
                                 phone=phone,
                                 quantity=cart.get(str(i.id)))
                     Order.save()
                     request.session['cart']={}
              return redirect('cart')   

@csrf_exempt
def signin(request):
        
        if request.method == 'GET':
           return render(request,'signin.html')
        else:
               postData=request.POST
               full_name =postData.get('username')
               phone=postData.get('Phone')
               email=postData.get('email')
               password=postData.get('password')
               Customer= customer(full_name=full_name,phone=phone,email=email,password=password)
              
               
               #velidation
               error_massage=''
               if len(phone)<10:
                      error_massage="Phone Number must be 10 char long.."
               elif  Customer.isExist():
                      error_massage="Email Adress already registered.."
               #saving
        if(not error_massage):  
                  Customer.password=make_password(Customer.password)
                  Customer.save()           
                 
                  return  render(request,'Home.html')
               
        return render(request,'signin.html',{'error':error_massage})
        
@csrf_exempt
def login(request):
        if request.method == 'GET':
           return render(request,'login.html')
        else:
               email=request.POST.get('email')
               password=request.POST.get('password')
               Customer=customer.get_customer_by_email(email)
               if Customer:
                   flag=check_password(password,Customer.password)
                   if flag:
                         request.session['Customer']=Customer.id
                        

                         return redirect('Home')
                  
               
               return render(request,'login.html',{'error':'Invalid login credentials'})

class categories(View):       
              
       def post(self,request):
              product=request.POST.get('product')
              remove=request.POST.get('remove')
              cart=request.session.get('cart')
              if cart:
                    quantity=cart.get(product)
                    if quantity:
                           if remove:
                                  if quantity<=1:
                                         cart.pop(product)
                                  else: cart[product]=quantity-1
                           else: 
                                  cart[product]=quantity+1
                    else:
                           cart[product]=1       
              else:
                     cart={}
                     cart[product]=1
              request.session['cart']=cart
              print(request.session['cart'])     
              return redirect('categories')
            
       def get(self,request):
          cart=request.session.get('cart')
          if not cart:
                 request.session['cart']={}
          products=None      
          categories =categorie.objects.all()
          catId= request.GET.get('categorie')
          if catId:
              products=Product.get_all_products_by_category_id(catId)
          else:
              products=Product.objects.all()
             
              print('you are:',request.session.get('email'))      
              return render(request,'categories.html',{'products':products,'categories':categories})  

def logout(request):
       request.session.clear()
       return redirect('Login')

def check(request):
       return render(request,'check.html')

class pizza(View):       
              
       def post(self,request):
              product=request.POST.get('product')
              remove=request.POST.get('remove')
              cart=request.session.get('cart')
              if cart:
                    quantity=cart.get(product)
                    if quantity:
                           if remove:
                                  if quantity<=1:
                                         cart.pop(product)
                                  else: cart[product]=quantity-1
                           else: 
                                  cart[product]=quantity+1
                    else:
                           cart[product]=1       
              else:
                     cart={}
                     cart[product]=1
              request.session['cart']=cart
              print(request.session['cart'])     
              return redirect('pizza')
            
       def get(self,request):
          cart=request.session.get('cart')
          if not cart:
                 request.session['cart']={}
          products=None      
          categories =categorie.objects.filter(id=2)
          catId= request.GET.get('pizza')
          if catId:
              products=Product.get_all_products_by_category_id(catId)
          else:
              products=Product.objects.filter(categorie_id=2)
             
              print('you are:',request.session.get('email'))      
              return render(request,'pizza.html',{'products':products,'categories':categories})  


class nonvegpizza(View):       
              
       def post(self,request):
              product=request.POST.get('product')
              remove=request.POST.get('remove')
              cart=request.session.get('cart')
              if cart:
                    quantity=cart.get(product)
                    if quantity:
                           if remove:
                                  if quantity<=1:
                                         cart.pop(product)
                                  else: cart[product]=quantity-1
                           else: 
                                  cart[product]=quantity+1
                    else:
                           cart[product]=1       
              else:
                     cart={}
                     cart[product]=1
              request.session['cart']=cart
              print(request.session['cart'])     
              return redirect('nonvegpizza')
            
       def get(self,request):
          cart=request.session.get('cart')
          if not cart:
                 request.session['cart']={}
          products=None      
          categories =categorie.objects.filter(id=3)
          catId= request.GET.get('nonvegpizza')
          if catId:
              products=Product.get_all_products_by_category_id(catId)
          else:
              products=Product.objects.filter(categorie_id=3)
             
              print('you are:',request.session.get('email'))      
              return render(request,'nonvegpizza.html',{'products':products,'categories':categories})  


class cheesepizza(View):       
              
       def post(self,request):
              product=request.POST.get('product')
              remove=request.POST.get('remove')
              cart=request.session.get('cart')
              if cart:
                    quantity=cart.get(product)
                    if quantity:
                           if remove:
                                  if quantity<=1:
                                         cart.pop(product)
                                  else: cart[product]=quantity-1
                           else: 
                                  cart[product]=quantity+1
                    else:
                           cart[product]=1       
              else:
                     cart={}
                     cart[product]=1
              request.session['cart']=cart
              print(request.session['cart'])     
              return redirect('cheesepizza')
            
       def get(self,request):
          cart=request.session.get('cart')
          if not cart:
                 request.session['cart']={}
          products=None      
          categories =categorie.objects.filter(id=4)
          catId= request.GET.get('cheesepizza')
          if catId:
              products=Product.get_all_products_by_category_id(catId)
          else:
              products=Product.objects.filter(categorie_id=4)
             
              print('you are:',request.session.get('email'))      
              return render(request,'cheesepizza.html',{'products':products,'categories':categories})  


class pepperonipizza(View):       
              
       def post(self,request):
              product=request.POST.get('product')
              remove=request.POST.get('remove')
              cart=request.session.get('cart')
              if cart:
                    quantity=cart.get(product)
                    if quantity:
                           if remove:
                                  if quantity<=1:
                                         cart.pop(product)
                                  else: cart[product]=quantity-1
                           else: 
                                  cart[product]=quantity+1
                    else:
                           cart[product]=1       
              else:
                     cart={}
                     cart[product]=1
              request.session['cart']=cart
              print(request.session['cart'])     
              return redirect('pepperonipizza')
            
       def get(self,request):
          cart=request.session.get('cart')
          if not cart:
                 request.session['cart']={}
          products=None      
          categories =categorie.objects.filter(id=1)
          catId= request.GET.get('pepperonipizza')
          if catId:
              products=Product.get_all_products_by_category_id(catId)
          else:
              products=Product.objects.filter(categorie_id=1)
             
              print('you are:',request.session.get('email'))      
              return render(request,'pepperonipizza.html',{'products':products,'categories':categories})  


class margheritapizza(View):       
              
       def post(self,request):
              product=request.POST.get('product')
              remove=request.POST.get('remove')
              cart=request.session.get('cart')
              if cart:
                    quantity=cart.get(product)
                    if quantity:
                           if remove:
                                  if quantity<=1:
                                         cart.pop(product)
                                  else: cart[product]=quantity-1
                           else: 
                                  cart[product]=quantity+1
                    else:
                           cart[product]=1       
              else:
                     cart={}
                     cart[product]=1
              request.session['cart']=cart
              print(request.session['cart'])     
              return redirect('margheritapizza')
            
       def get(self,request):
          cart=request.session.get('cart')
          if not cart:
                 request.session['cart']={}
          products=None      
          categories =categorie.objects.filter(id=5)
          catId= request.GET.get('margheritapizza')
          if catId:
              products=Product.get_all_products_by_category_id(catId)
          else:
              products=Product.objects.filter(categorie_id=5)
             
              print('you are:',request.session.get('email'))      
              return render(request,'margheritapizza.html',{'products':products,'categories':categories})  


class supremepizza(View):       
              
       def post(self,request):
              product=request.POST.get('product')
              remove=request.POST.get('remove')
              cart=request.session.get('cart')
              if cart:
                    quantity=cart.get(product)
                    if quantity:
                           if remove:
                                  if quantity<=1:
                                         cart.pop(product)
                                  else: cart[product]=quantity-1
                           else: 
                                  cart[product]=quantity+1
                    else:
                           cart[product]=1       
              else:
                     cart={}
                     cart[product]=1
              request.session['cart']=cart
              print(request.session['cart'])     
              return redirect('supremepizza')
            
       def get(self,request):
          cart=request.session.get('cart')
          if not cart:
                 request.session['cart']={}
          products=None      
          categories =categorie.objects.filter(id=6)
          catId= request.GET.get('supremepizza')
          if catId:
              products=Product.get_all_products_by_category_id(catId)
          else:
              products=Product.objects.filter(categorie_id=6)
             
              print('you are:',request.session.get('email'))      
              return render(request,'supremepizza.html',{'products':products,'categories':categories})  


class sides(View):       
              
       def post(self,request):
              product=request.POST.get('product')
              remove=request.POST.get('remove')
              cart=request.session.get('cart')
              if cart:
                    quantity=cart.get(product)
                    if quantity:
                           if remove:
                                  if quantity<=1:
                                         cart.pop(product)
                                  else: cart[product]=quantity-1
                           else: 
                                  cart[product]=quantity+1
                    else:
                           cart[product]=1       
              else:
                     cart={}
                     cart[product]=1
              request.session['cart']=cart
              print(request.session['cart'])     
              return redirect('sides')
            
       def get(self,request):
          cart=request.session.get('cart')
          if not cart:
                 request.session['cart']={}
          products=None      
          categories =categorie.objects.filter(id=7)
          catId= request.GET.get('sides')
          if catId:
              products=Product.get_all_products_by_category_id(catId)
          else:
              products=Product.objects.filter(categorie_id=7)
             
              print('you are:',request.session.get('email'))      
              return render(request,'sides.html',{'products':products,'categories':categories})  



 


 


 


 


 


 
 


 


 


 


 


 


 
 


 


 


 


 


 


 


 


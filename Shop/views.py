from django.shortcuts import render, redirect
from . models import Customer, Product, Card, OrderPlaced
from django.views import View
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.
# def home(request):
#      return render(request, 'Shop/home.html')

class ProdctView(View):
 def get(self, request):
  gentspants = Product.objects.filter(category = 'GP')
  borkhas = Product.objects.filter(category = 'BK')
  babyFushions = Product.objects.filter(category = "BF")
  return render(request, 'Shop/home.html',{'gentspants': gentspants, 'borkhas': borkhas, 'babyFushions': babyFushions })

# def product_detail(request):
#  return render(request, 'Shop/productdetail.html')

class ProductDetailsView(View):
 def get(self, request, pk):
  product =  Product.objects.get(pk=pk)
  return render(request, 'Shop/productdetail.html', {'product':product})

def add_to_cart(request):
 user = request.user
 product_id = request.GET.get('prod_id')
 product = Product.objects.get(id = product_id)
 addCardProdcut = Card(user=user, product=product)
 addCardProdcut.save()
 return redirect('/cart/')

def show_card(request):
 if request.user.is_authenticated:
  user =request.user

  amount = 0
  shipping_amount =100
  total_amount = 0
  cart_product = [p for p in Card.objects.all() if p.user == user]
  
  if cart_product:
   for p in cart_product:
    temp_amount = (p.quantity * p.product.discounted_price)
    amount = temp_amount + amount
    totalamount = amount + shipping_amount
  else:
   return render(request, 'Shop/emptycart.html')
   
  cart = Card.objects.filter(user=user)
  return render(request, 'Shop/addtocart.html', {'carts':cart, 'totalamount': totalamount, 'amount':amount})
 

def plus_cart(request):
 if request.method == "GET":
  prod_id = request.GET['prod_id']
  c = Card.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity +=1
  c.save()

  amount = 0
  shopping_amount = 100
  cart_product = [p for p in Card.objects.all() if p.user == request.user]
  for p in cart_product:
   tempamount = (p.quantity * p.product.discounted_price)
   amount += tempamount
   totalamount = amount + shopping_amount

   data = {
     'quantity': c.quantity,
     'amount': amount,
     'totalamount': totalamount,
    }

   return JsonResponse(data)
   

def minus_cart(request):
 if request.method == "GET":
  prod_id = request.GET['prod_id']
  c = Card.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.quantity -=1
  c.save()

  amount = 0
  shopping_amount = 100
  cart_product = [p for p in Card.objects.all() if p.user ==  request.user]
  if cart_product:
   for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount
    totalamount = amount + shopping_amount

    data = {
     'quantity': c.quantity,
     'amount': amount,
     'totalamount': totalamount
    }

    return JsonResponse(data)
   
  
def remove_cart(request):
 if request.method == "GET":
  prod_id = request.GET['prod_id']
  c = Card.objects.get(Q(product=prod_id) & Q(user=request.user))
  c.delete()

  amount = 0
  shopping_amount = 100
  cart_product = [p for p in Card.objects.all() if p.user ==  request.user]
  if cart_product:
   for p in cart_product:
    tempamount = (p.quantity * p.product.discounted_price)
    amount += tempamount
    totalamount = amount + shopping_amount

    data = {
     'amount': amount,
     'totalamount': totalamount
    }

    return JsonResponse(data)


def buy_now(request):
 return render(request, 'Shop/buynow.html')

# def profile(request):
#  return render(request, 'Shop/profile.html')

class Profile_View(View):
 def get(self, request):
  form = CustomerProfileForm()
  return render(request, 'Shop/profile.html',{'form':form, 'active':'btn-primary'})
 
 def post(self, request):
  form = CustomerProfileForm(request.POST)
  if form.is_valid():
    usr = request.user
    name = form.cleaned_data['name']
    division = form.cleaned_data['division']
    district = form.cleaned_data['district']
    thana = form.cleaned_data['thana']
    villorroad = form.cleaned_data['villorroad']
    zipCode = form.cleaned_data['zipCode']
    reg = Customer(user=usr,name=name, division=division,district=district,thana=thana,villorroad=villorroad, zipCode=zipCode)
    reg.save()
    messages.success(request, 'this is profile update successfull done !')
  return render(request, 'Shop/profile.html',{'form':form, 'active':'btn-primary'})

def address(request):
 add = Customer.objects.filter(user=request.user)
 return render(request, 'Shop/address.html', {'add':add, 'active':'btn-primary'})

def orders(request):
 current_order_place = OrderPlaced.objects.filter(user = request.user)
 return render(request, 'Shop/orders.html', {'order_placed':current_order_place})

def change_password(request):
 return render(request, 'Shop/changepassword.html')

def lehenga(request, data=None):
  if data == None:
    lehengas = Product.objects.filter(category = 'L')
  elif data == "intervalue" or data == "NSB":
    lehengas = Product.objects.filter(category ='L').filter(brand = data)
  elif data == 'below':
   lehengas = Product.objects.filter(category='L').filter(selling_price__lt = 500)
  elif data == 'Above':
   lehengas = Product.objects.filter(category = 'L').filter(selling_price__gt = 500)

  return render(request, 'Shop/lehenga.html', {'lehengas':lehengas})





# def customerregistration(request):
#  return render(request, 'Shop/customerregistration.html')

class customerRegistrationView(View):
 def get(self, request):
  form = CustomerRegistrationForm()
  return render(request, 'Shop/customerregistration.html', {'form':form})
 
 def post(self, request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   form.save()
   messages.success(request, 'registraton successfully complated !')
  return render(request, 'Shop/customerregistration.html', {'form':form})

# def login(request):
#     return render(request, 'Shop/login.html')



def checkout(request):
  user = request.user
  add = Customer.objects.filter(user = user)
  cart_item = Card.objects.filter(user = user)
  amount = 0
  shipping_amount = 100
  totalamount = 0
  cart_product = [ p for p in Card.objects.all() if p.user == user]
  for p in cart_product:
    temp_amount = (p.quantity * p.product.discounted_price)
    amount += temp_amount
    totalamount = amount + shipping_amount
  return render(request, 'Shop/checkout.html', {'add':add, 'totalamount':totalamount, 'cart_item': cart_item})


def payment_done(request):
  user = request.user
  customer_id = request.GET.get("customer_id")
  customer = Customer.objects.get(id = customer_id)
  carts = Card.objects.filter(user = user)
  for cart in carts:
   place_order = OrderPlaced(user = user, Customer=customer,  product=cart.product, quantity=cart.quantity)
   place_order.save()
   cart.delete()
  return redirect('/orders/')
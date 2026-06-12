from django.shortcuts import render
from . models import Customer, Product, Card, OrderPlaced
from django.views import View
from . forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages

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
 return render(request, 'Shop/addtocart.html')

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
    user = request.user
    division = form.cleaned_data['division']
    district = form.cleaned_data['district']
    thana = form.cleaned_data['thana']
    villorroad = form.cleaned_data['villorroad']
    zipCode = form.cleaned_data['zipCode']
    reg = Customer(user=user,division=division,district=district,thana=thana,villorroad=villorroad, zipCode=zipCode)
    reg.save()
    messages.success(request, 'this is profile update successfull done !')
  return render(request, 'Shop/profile.html',{'form':form, 'active':'btn-primary'})

def address(request):
 return render(request, 'Shop/address.html')

def orders(request):
 return render(request, 'Shop/orders.html')

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
 return render(request, 'Shop/checkout.html')

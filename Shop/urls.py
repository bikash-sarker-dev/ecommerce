from django.urls import path
from Shop import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . forms import LoginForm, ChangePasswordFrom, PasswordResetForm

urlpatterns = [
    path('', views.ProdctView.as_view(), name = 'home'),
    # path('product-detail/', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>', views.ProductDetailsView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),


    # path('changepassword/', views.change_password, name='changepassword'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name = "Shop/changepassword.html", form_class = ChangePasswordFrom,  success_url='/changepassworddone/'), name='changepassword'),
    path('changepassworddone/', auth_views.PasswordChangeView.as_view(template_name="Shop/changepasswordDone.html"), name='changepassworddone'),


    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="Shop/password_reset.html", form_class=PasswordResetForm), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'Shop/password_reset_done.html'), name="password_reset_done"),
    path('lehenga/', views.lehenga, name='lehenga'),

    path('lehenga/<slug:data>', views.lehenga, name='lehengaItem' ),
    # path('login/', views.login, name='login'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='Shop/login.html', authentication_form = LoginForm), name="login"),


    path('registration/', views.customerRegistrationView.as_view(), name='customerregistration'),



    path('checkout/', views.checkout, name='checkout'),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'login') , name="logout"),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
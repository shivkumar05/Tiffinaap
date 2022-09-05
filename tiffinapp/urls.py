"""tiffinproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from atexit import register
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from tiffinapp.view.manu import AddMannu , Edit , Filtercategery
from tiffinapp.view.user import Account1 , sig  , UserListView  , RegisterUser , EditProfile
from tiffinapp.view.cart import CartView
from tiffinapp.view.changepass import ChangePasswordView
from tiffinapp.view.changeemail import ChangeEmailView
from tiffinapp.view.category import Category
from tiffinapp.view.forpass import Home ,Login , Register , ForgetPassword , ChangePassword , Logout
from tiffinapp.view.timezon import set_timezone
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('editprofile/<int:pk>',EditProfile.as_view()),
    path('account',Account1.as_view()),
    path('sigin',sig.as_view()),
    path('add_manu',AddMannu.as_view()),
    path('editmanu/<int:pk>' ,Edit.as_view()),
    path('user', UserListView.as_view() ),
    path('filter/',Filtercategery.as_view()),
    path('cart' ,CartView.as_view()),
    path('regis/' , RegisterUser.as_view()),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    #path('api/change-email/', ChangeEmailView.as_view(), name='change-email'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('change_email/<int:pk>/', ChangeEmailView.as_view(), name='auth_change_password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path("password-reset-confirm/<uidb64>/<token>/",auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('' , Home , name="home"),
    path('login/' , Login , name="login"),
    path('register/' , Register , name="register"),
    path('forget-password/' , ForgetPassword , name="forget_password"),
    path('change-password/<token>/' , ChangePassword , name="change_password"),
    path('logout/' , Logout , name="logout"),
    path('time/' , set_timezone , name="set_timezone"),
    # path('sig/',Sigin.as_view()),
    
   
]+static(settings.MEDIA_URL , document_root= settings.MEDIA_ROOT)

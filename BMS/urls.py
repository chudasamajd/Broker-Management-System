"""BMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
path('',views.index),
    path('index',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('contactdata',views.contactData),
    path('registration',views.registration),
    path('registrationdata',views.registrationdata),
    path('login',views.login),
    path('logindata',views.loginData),
    path('logout',views.logout),
    path('forsell',views.forsell),
    path('forselldata',views.forselldata),
    path('forrent',views.forrent),
    path('forrentdata',views.forrentdata),
    path('buy',views.buy),
    path('buysingle/<pid>',views.buySingle),
    path('purchaseRequest',views.purchaseRequest),
    path('rent',views.rent),
    path('rentsingle/<pid>',views.rentSingle),
    path('rentRequest',views.rentRequest),
    path('profile',views.profile),
]

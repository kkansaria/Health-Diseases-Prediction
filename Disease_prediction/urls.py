"""Disease_prediction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import to :  from my_app import views
    2. Add a URL to urlpatterns to :  path('', views.home, name='home')
Class-based views
    1. Add an import to :  from other_app.views import Home
    2. Add a URL to urlpatterns which is :  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns to :   path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
     path('admin/', admin.site.urls),
     path("", include("prediction_model.urls")),
     path("accounts/", include("authy.urls")),
]

"""
URL configuration for project10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from productapp.views import Home,ProdutInput,ProductInsert,ProductsDisplay,ProductUpdateInput,ProuductUpdateDetails,\
    Update,ProductDeleteInput,ProductDelete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mymart',Home.as_view()),
    path('productinput',ProdutInput.as_view()),
    path('productinsert',ProductInsert.as_view()),
    path('productsdisplay',ProductsDisplay.as_view()),
    path('productupdateinput',ProductUpdateInput.as_view()),
    path('prouductupdatedetails',ProuductUpdateDetails.as_view()),
    path('update',Update.as_view()),
    path('productdeleteinput',ProductDeleteInput.as_view()),
    path('productdelete',ProductDelete.as_view()),
]

"""Django_4m URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the iinclude() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import main_view, products_view, detail_view, category_view, create_products
from django.conf.urls.static import static
# from Blog.settings import MEDIA_ROOT,MEDIA_URL
from Django_4m.settings import MEDIA_URL, MEDIA_ROOT
from users.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view),
    path('products/<int:id>/', detail_view),
    path('categories/', category_view),
    path('products/create/', create_products),
    path('users/login/', login_view),
    path('users/register/', register_view),
    path('users/logout/', login_view),

]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)





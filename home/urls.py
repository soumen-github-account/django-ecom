"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path,  include

from django.conf import settings
from django.conf.urls.static import static

from store.views import *

urlpatterns = [
    path('main/', home, name='home'),
    path('collections/<str:cslug>', collection, name='col'),
    path('product/<str:prod_name>/<str:pslug>/',ok , name='product-page'),
    path('cart.html/',cart, name="carts"),
    path('',signin, name='signin'),
    path('signup.html/',signup, name='signup'),
    path('logout/', Logout, name="log"),
    path('add-to-cart',addto , name="addto"),
    path('delete-cart-item',delete , name="delete-cart-item"),
    path('checkout', checkout,name='checkout'),
    path('place-order', placeorder,name='placeorder'),
    path('my-order', myorders,name='myorders'),
    path('order-view/<str:t_no>/', orderview,name='orderview'),
    path('product-list', productlistajax),
    path('searchproducts', searchproduct, name="searchproducts"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
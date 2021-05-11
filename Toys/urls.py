from django.urls import path
from Toys import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from .views import *

urlpatterns = [
    path('login/',views.login,name="login"),
    path('home/',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('cart/',views.cart,name="cart"),
	path('checkout/',views.checkout,name="checkout"),
	path('contact/',views.contact,name="contact"),
	path('myAccount/',views.myAccount,name="myAccount"),
	path('productDetail/',views.productDetail,name="productDetail"),
	path('productList/',views.productList,name="productList"),
	path('wishlist/',views.wishlist,name="wishlist"),
	
    
    path('image_upload/', hotel_image_view, name = 'image_upload'),
    path('success/', success, name = 'success'),
    path('hotel_images', display_hotel_images, name = 'hotel_images'),



    

]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


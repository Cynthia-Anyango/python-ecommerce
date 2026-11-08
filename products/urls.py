from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
]




# path() defines a URL route.
# '' means the default URL for this app.
# views.product_list tells Django which function to execute.
# name='product_list' gives the URL a reusable name.
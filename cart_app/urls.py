from django.urls import path
from . import views

app_name = 'cart_app'

urlpatterns = [

    path('',views.Search_result,name='Search_result'),

]

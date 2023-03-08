from . import views
from django.urls import path

app_name = 'Stoneapp'

urlpatterns = [

    path('',views.all_Product_Category,name='all_Product_Category'),
    path('<slug:c_slug>/',views.all_Product_Category,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.Product_Details,name='Product_Details'),

]
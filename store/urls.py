from django.urls import path

from store import views

app_name = 'store'

urlpatterns = [
    path('shop/', views.shop, name='shop'),
    path('<str:slug>/', views.product_deal_create, name='product_detail'),
    path('des/<str:slug>/', views.product_desc, name='product_desc'),

    path('list', views.objetdeals_list, name='list_deal'),
    path('deal_det/<str:imei>', views.objetdeal_detail, name='objetdeal_detail'),
    path('objdeal/<str:imei>', views.update_objetdeal, name='update_objetdeal'),
    path('objdeal_del/<str:imei>', views.delete_objetdeal, name='delete_objetdeal'),
]

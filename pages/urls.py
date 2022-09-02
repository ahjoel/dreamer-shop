from django.urls import path

from pages import views

from accounts import views as view_account

app_name = 'pages'

urlpatterns = [
    path('', views.home, name='home'),
    # path('', view_account.login_view, name='login'),
    path('shop', views.shop, name='shop'),
    path('product', views.product, name='product'),
]

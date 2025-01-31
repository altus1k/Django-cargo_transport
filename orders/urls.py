# filepath: /home/danial/projects/Doni/cargo_transport/orders/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('orders/', views.orders_list, name='orders_list'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<int:order_id>/', views.update_order, name='update_order'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),
    path('profile/', views.profile, name='profile'),
    path('add_driver/', views.add_driver, name='add_driver'),
]
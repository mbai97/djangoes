from django.urls import path

from playground.views import fashion, jewellery
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('index', views.index, name='index'),
    path('jewellery', views.jewellery, name='jewellery'),
    path('fashion', views.fashion, name='fashion'),
    path("electronic", views.electronic, name="electronic")
    
]
 
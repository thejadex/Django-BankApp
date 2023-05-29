from django.urls import path
from . import views 


urlpatterns = [
    path('', views.homepage, name='homepage'), # Default View
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name="logout"),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('transfer/', views.transfer, name='transfer'),
]

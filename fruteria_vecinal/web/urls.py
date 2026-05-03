from django.urls import path
from .views import index   
from web.views import CustomLoginView, CustomLogoutView, RegisterView

urlpatterns = [
    path('', index, name='index'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
]

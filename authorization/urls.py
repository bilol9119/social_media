
from django.urls import path
from .views import signup_view, login_view, logout_view


urlpatterns = [
    path('auth/login/', login_view, name='login'),
    path('auth/register/', signup_view, name='register'),
    path('auth/logout/', logout_view, name='logout'),
]
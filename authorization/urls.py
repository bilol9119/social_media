
from django.urls import path
from .views import signup_view, login_view, logout_view


urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', signup_view, name='register'),
    path('logout/', logout_view, name='logout'),
]
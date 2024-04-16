from django.urls import path
from .views import logout_view, login_view, register_view


urlpatterns = [
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
]
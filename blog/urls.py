from django.urls import path
from .views import (home_view, search_view,
                    post_comment_view, profile_view,
                    like_view, accaunt_settings_view, follow)

urlpatterns = [
    path('', home_view, name='home'),
    path('search/', search_view),
    path('post_comment/', post_comment_view),
    path('profile/<int:pk>/', profile_view),
    path('like/<int:pk>/', like_view),
    path('accaunt/', accaunt_settings_view),
    path('follow/<int:pk>/', follow),
]
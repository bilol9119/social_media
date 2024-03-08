from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (home_view, account_settings_view,
                    profile_view, following_view,
                    comment_save)


urlpatterns = [
    path('', home_view, name='home'),
    path('account/', account_settings_view, name='account'),
    path('profile/', profile_view, name='profile'),
    path('follow/<int:id>/', following_view, name='follow'),
    path('commentsave', comment_save, name='commentsave'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
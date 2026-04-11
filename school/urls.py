from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, redirect
from django.conf import settings
from django.conf.urls.static import static
import schoolviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schoolviews.redirect_to_login),
    path('login/', schoolviews.redirect_to_login),
    path('login/<slug:user_type>/', schoolviews.login, name='portal-login'),
    path('signup/', schoolviews.redirect_to_signup),
    path('signup/<slug:user_type>/', schoolviews.signup, name='portal-signup'),
    path('studentportal/', include('studentportal.urls')),
    path('teacherportal/', include('teacherportal.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views
from schoolviews import redirect_to_login
urlpatterns = [
    path('', redirect_to_login),
    path('s/', redirect_to_login),
    path('s/<slug:username>/', views.home, name='home'),
    path('<str:username>/upload-picture/', views.upload_picture, name='upload-picture'),
    path('<str:username>/', views.home, name='home'),
]
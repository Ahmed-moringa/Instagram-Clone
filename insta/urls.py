from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
]
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name= 'index'),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('profile/<username>/', views.profile, name='profile'),
    path('search/', views.search_profile, name='search'),
    path('post/<id>', views.post_comment, name='comment'),
]
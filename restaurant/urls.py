from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('book/', views.book, name="book"),
    path('menu_item/<int:pk>', views.menu_item, name="menu_item"),
    # Add the remaining URL path configurations here
]
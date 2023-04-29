from django.urls import path
from .views import menu, navbarview

urlpatterns = [
    path('navbar/',menu,name="menu"),
    path('',navbarview,name="navbar"),
]
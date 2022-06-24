from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
   path("",home,name="home"),
   path("login/",login,name="login"),
   path("signup/",signup,name="signup"),
   path("add-suggestion/",add_suggestion),
   path('logout/',signout),
   path("delete-sug/<int:id>/",delete_sug)
]

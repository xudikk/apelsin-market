from django.urls import path
from .views import index
from core.services import auth

urlpatterns = [
    path("", index, name="home"),


    #auth
    path("login/", auth.sign_in, name='login'),

]

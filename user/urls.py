from django.urls import path
from user import views

#name으로 url대체하기 위해서
app_name = 'user'

urlpatterns = [
    path("signup/", views.signup, name='signup'),
    path("login/", views.login, name='login'),
    path("home/", views.home, name='home'),
]

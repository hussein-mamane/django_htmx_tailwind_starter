from django.urls import path,include
from mainapp import views

app_name = 'mainapp'
urlpatterns = [
    path("", views.home, name="home"),
]
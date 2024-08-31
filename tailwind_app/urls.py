from django.urls import path,include
from tailwind_app import views

urlpatterns = [
    path('',views.tlwnd,name='home'),
]
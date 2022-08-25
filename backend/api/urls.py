from django.urls import path
from . import views


   

urlpatterns = [
   path('',views.api_home),
   path('test/',views.api_home1)
]
   
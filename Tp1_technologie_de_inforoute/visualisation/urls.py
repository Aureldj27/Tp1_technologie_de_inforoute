from  .views import home,search_view
from django.urls import path,include

urlpatterns = [
    path('',home,name="home"),
    path('recherche/', search_view, name='visualisation_home'),
   
]
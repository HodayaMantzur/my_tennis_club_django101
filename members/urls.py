<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('details/<int:id>', views.details, name='details'),
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('details/<int:id>', views.details, name='details'),
>>>>>>> 6a028d562591f51c2fd9f4d8900b788561431771
]
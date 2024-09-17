<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.courts, name='courts'),
    path('reserve/<int:id>', views.reserve, name='reserve'),
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.courts, name='courts'),
    path('reserve/<int:id>', views.reserve, name='reserve'),
]
>>>>>>> 6a028d562591f51c2fd9f4d8900b788561431771

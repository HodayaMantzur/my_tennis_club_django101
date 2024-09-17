<<<<<<< HEAD

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('courts/', include('courts.urls')),
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
]
=======

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('courts/', include('courts.urls')),
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
]
>>>>>>> 6a028d562591f51c2fd9f4d8900b788561431771

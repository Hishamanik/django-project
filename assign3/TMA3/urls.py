from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('part1/', include('part1.urls')),
    path('part2/', include('part2.urls')),
    path('part3/', include('part3.urls')),
    path('part4/', include('part4.urls')),
    path('admin/', admin.site.urls),
]
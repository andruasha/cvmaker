from django.contrib import admin
from django.urls import path
from home.views import index, home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/', home, name='home'),
]

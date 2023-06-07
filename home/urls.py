from django.urls import path
from home.views import index, home


app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
]
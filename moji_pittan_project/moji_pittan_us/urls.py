from django.urls import path
from . import views

app_name = 'moji_pittan_us'
urlpatterns = [
    path(r'', views.index, name='index'),
]
from django.urls import path
from . import views

app_name = 'num'
urlpatterns = [
    path('', views.HomeView.as_view(), name='form_num'),
    ]
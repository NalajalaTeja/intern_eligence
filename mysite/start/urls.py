from django.urls import path

from . import views

app_name = 'start'
urlpatterns = [
    path('', views.entry, name='entry'),
   path('success/',views.success,name='success')
]
from django.urls import path
from polls import views

urlpatterns = [
    path('', views.hello, name = 'polls'),
    path('polls2/', views.secondpolls, name = 'second polls'),
]
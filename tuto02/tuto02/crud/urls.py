from django.urls import path,include
from . import views
urlpatterns = [
    path('<int:pk>/',views.detail),
    path('create/',views.create),
    path('new/',views.new),
    path('',views.index),
]

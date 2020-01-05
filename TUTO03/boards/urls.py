from django.urls import path,include
from . import views
app_name = 'boards'
urlpatterns = [
    path('edit/<int:boards_pk>',views.edit, name='edit'),
    path('detail/<int:boards_pk>/delete',views.delete, name='delete'),
    path('detail/<int:boards_pk>',views.detail, name='detail'),
    path('new/',views.new, name='new'),
    path('',views.index, name='index'),
]

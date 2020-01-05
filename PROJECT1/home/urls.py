from django.urls import path
from . import views
urlpatterns= [
    path('static_example/',views.static_example),
    path('user_create/',views.user_create),
    path('user_new/',views.user_new),
    path('get/',views.get),
    path('throw/',views.throw),
    path('result/',views.result),
    path('catch/',views.catch),
    path('pong/',views.pong),
    path('ping/',views.ping),
    path('template_language/',views.template_language),
    path('introduce/<name>/<int:age>/',views.introduce),
    path('cube/<int:num>/',views.cube),
    path('hello/<name>/',views.hello),
    path('lottos/',views.lottos),
    path('midnight/',views.midnight),
    path('hola/',views.hola),
    path('index/',views.index),
]
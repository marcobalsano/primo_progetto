from importlib.resources import path


from django.urls import path
from prima_app.views import *

app_name="prima app"
urlpatterns=[
    path('homepage', homepage, name='homepage'),
    path('welcome', welcome, name='welcome'),
    path('lista', lista, name='lista'),
]
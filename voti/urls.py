from importlib.resources import path


from django.urls import path
from voti.views import *

app_name="voti"
urlpatterns = [
    path('', indexVoti, name='indexVoti'),
    path('view_a', view_a, name='materie'),
    path('view_b', view_b, name='dizionario'),
    path('view_c', view_c, name='media'),
]

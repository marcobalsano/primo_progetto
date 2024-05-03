"""
URL configuration for primo_progetto project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    
Add an import:  from my_app import views
Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    
Add an import:  from other_app.views import Home
Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    
Import the include() function: from django.urls import include, path
Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from .views import index 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('prima_app/',include("prima_app.urls", namespace="prima_app")),
    path('', index, name='index'),
    path('seconda_app/',include("seconda_app.urls", namespace="seconda_app")),
    path('news/', include("news.urls", namespace="news")),
    path('voti/', include("voti.urls", namespace="voti")),
    path('products/', include("products.urls", namespace="products")),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
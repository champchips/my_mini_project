"""my_mini_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import include, path
from django.conf import settings 
from django.conf.urls.static import static 
from polls import views as p_views
from authen import views as a_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', a_views.my_login, name='login'),
    path('', a_views.my_login, name='login'),
    path('register/', a_views.my_register, name='register'),
    path('index/', p_views.index, name='index'),
    path('polls/', include('polls.urls')),
    path('logout/', a_views.my_logout, name='logout'),
    # path('', include("django.contrib.auth.urls")),
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, 
    document_root=settings.MEDIA_ROOT)

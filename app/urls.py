"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic.base import TemplateView

from app.common_settings import ADMIN,DEBUG,ALLOWED_HOSTS, ENV
from app.settings import STATIC_ROOT, STATIC_URL
from app.views import index_view

urlpatterns = [
    re_path(r'', index_view),
    path(ADMIN, admin.site.urls),
    re_path(r'^(?:.*)/?$', index_view),
]

print("DEBUG: ",DEBUG)
print("ALLOWED_HOSTS: ",ALLOWED_HOSTS)
print("STATIC_ROOT: ",STATIC_ROOT)
print("STATIC_URL: ",STATIC_URL)
print("ENV: ",ENV)
if not DEBUG:    
    handler404 = 'error_handler.views.error_404'
    handler500 = 'error_handler.views.error_500'
    handler403 = 'error_handler.views.error_403'
    handler400 = 'error_handler.views.error_400'
else:
    from django.conf.urls.static import static
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)

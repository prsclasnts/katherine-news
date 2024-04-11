"""
URL configuration for katherine_news project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.http import HttpResponse
from django.urls import path, include
from app_users.views import home, about
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home),
    path("about/", about),
    path("users/", include("app_users.urls")),
    path("", include("app_authors.urls")),
    path("", include("app_categories.urls")),
    path("news/", include("app_news.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

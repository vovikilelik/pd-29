"""siesta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ads.views import Hello, AdsViewSet
from categories.views import CategoriesViewSet
from locations.views import LocationsViewSet
from siesta import settings
from users.views import UsersViewSet

router = routers.SimpleRouter()

router.register('users', UsersViewSet)
router.register('locations', LocationsViewSet)
router.register('categories', CategoriesViewSet)
router.register('ads', AdsViewSet)

urlpatterns = [
    path('', Hello.as_view()),
    path('admin/', admin.site.urls),
    path('ads/', include('ads.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

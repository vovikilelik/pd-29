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
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from ads.views import AdsViewSet, CategoriesViewSet
from selections.views import SelectionsViewSet
from siesta import settings
from users.views import UsersViewSet, LocationsViewSet, LogoutView

router = routers.SimpleRouter()

router.register('users', UsersViewSet)
router.register('locations', LocationsViewSet)
router.register('categories', CategoriesViewSet)
router.register('ads', AdsViewSet)
router.register('selections', SelectionsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', obtain_auth_token),  # Token Auth
    path('logout/', LogoutView.as_view()),  # Token Auth
    path('token/', TokenObtainPairView.as_view()),  # JWT Auth
    path('token/refresh/', TokenRefreshView.as_view()),  # JWT Auth
    path('ads/', include('ads.urls')),
]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

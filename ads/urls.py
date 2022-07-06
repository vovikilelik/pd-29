from django.urls import path

from ads.views import AdImageUpload

urlpatterns = [
    path('<int:pk>/upload/', AdImageUpload.as_view()),
]

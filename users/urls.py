from django.urls import path

from ads.views import AdImageUpload
from users.views import UsersListView, UserDetailView, UserUpdateView, UserDestroyView, UserCreateView

urlpatterns = [
    path('', UsersListView.as_view()),
    path('<int:pk>', UserDetailView.as_view()),
    path('<int:pk>/update/', UserUpdateView.as_view()),
    path('<int:pk>/create/', UserCreateView.as_view()),
    path('<int:pk>/delete/', UserDestroyView.as_view()),
]

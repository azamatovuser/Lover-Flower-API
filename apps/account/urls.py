from django.urls import path
from .views import RegisterAPIView, LoginAPIView, RUDAPIView


urlpatterns = [
    path('account/register/', RegisterAPIView.as_view()),
    path('account/login/', LoginAPIView.as_view()),
    path('account/<int:pk>/', RUDAPIView.as_view()),
]
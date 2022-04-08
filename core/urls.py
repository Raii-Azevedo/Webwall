from django.urls import path
from .views import CicloAPIView, CiclosAPIView


urlpatterns = [
    path('ciclos/<int:pk>/', CiclosAPIView.as_view(), name='ciclos'),
    path('ciclos/', CicloAPIView.as_view(), name='ciclo'),
]

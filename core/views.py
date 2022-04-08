from rest_framework import generics
from .models import Ciclo
from .serializers import CicloSerializer


class CicloAPIView(generics.ListCreateAPIView):
    queryset = Ciclo.objects.all()
    serializer_class = CicloSerializer


class CiclosAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ciclo.objects.all()
    serializer_class = CicloSerializer

    def get_queryset(self):
        if self.kwargs.get('ciclo_pk'):
            return self.queryset.filter(ciclo_id=self.kwargs.get('ciclo_pk'))
        return self.queryset.all()


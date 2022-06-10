import codecs
import csv

from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage

from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from .serializers import CicloSerializer

from .models import Ciclo

fs = FileSystemStorage(location='tmp/')


# Viewset
class CicloViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing the Ciclo data.
    """
    queryset = Ciclo.objects.all()
    serializer_class = CicloSerializer

    @action(detail=False, methods=['POST'])
    def upload_data(self, request):
        file = request.FILES['file']

        content = file.read()
        file_content = ContentFile(content)
        file_name = fs.save(
            "tmp.csv", file_content
        )
        tmp_file = fs.path(file_name)

        csv_file = open(tmp_file, errors="ignore")
        reader = csv.reader(csv_file)
        next(reader)

        ciclos_list = []

        for id, row in enumerate(reader):
            (
                tipo_kmep_id,
                data_atual,
                tkm_d,
                parada_d,
                kmep_d,
                tkm_acum,
                parada_acum,
                kmep_acum,
            ) = row

            ciclos_list.append(
                Ciclo(
                    tipo_kmep=tipo_kmep_id,
                    data_atual=data_atual,
                    tkm_d=tkm_d,
                    parada_d=parada_d,
                    kmep_d=kmep_d,
                    tkm_acum=tkm_acum,
                    parada_acum=parada_acum,
                    kmep_acum=kmep_acum,
                )
            )
        Ciclo.objects.bulk_create(ciclos_list)

        return Response("CSV carregado corretamente")

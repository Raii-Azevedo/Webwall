from django.db import models
from django.conf import settings


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ciclo(Base):
    tipo_kmep = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tipo_kmep', null=True
    )
    data_atual = models.DateTimeField(auto_now=True)
    tkm_d = models.DecimalField(max_digits=8, decimal_places=3)
    parada_d = models.IntegerField()
    kmep_d = models.DecimalField(max_digits=8, decimal_places=3)
    tkm_acum = models.IntegerField()
    parada_acum = models.IntegerField()
    kmep_acum = models.DecimalField(max_digits=8, decimal_places=3)

    class Meta:
        verbose_name = 'ciclo'
        verbose_name_plural = 'ciclos'

    def __str__(self):
        return self.tipo_kmep

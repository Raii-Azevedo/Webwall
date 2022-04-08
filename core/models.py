from django.db import models


class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Ciclo(Base):
    titulo = models.CharField(max_length=200)
    url = models.URLField(unique=True)
    indicador = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'ciclo'
        verbose_name_plural = 'ciclos'

    def __str__(self):
        return self.titulo

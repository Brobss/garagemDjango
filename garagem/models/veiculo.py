from django.db import models

from . import Cor, Acessorio, Modelo

from uploader.models import Image


class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    acessorios = models.ManyToManyField(Acessorio)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)

    imagens = models.ManyToManyField(
        Image,
        related_name="+",
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.modelo

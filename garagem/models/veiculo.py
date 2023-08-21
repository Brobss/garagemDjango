from django.db import models

from . import Marca, Categoria, Cor, Acessorio

from uploader.models import Image


class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    acessorios = models.ManyToManyField(Acessorio)
    modelo = models.CharField(max_length=50)
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

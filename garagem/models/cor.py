from django.db import models


class Cor(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao

from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50, default='')
    nacionalidade = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nome.upper()

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
    
class Cor(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao
    
    class Meta:
        verbose_name_plural = 'Cores'

class Acessorio(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao
    
class Veiculo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    cor = models.ForeignKey(Cor, on_delete=models.CASCADE)
    acessorios = models.ManyToManyField(Acessorio)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.modelo
from django.db import models

# Create your models here.

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    duracao = models.IntegerField()  
    ano_lancamento = models.IntegerField()
    sinopse = models.TextField()
    imagem = models.ImageField(upload_to='filmes/imagens/')

    def __str__(self):
        return self.titulo
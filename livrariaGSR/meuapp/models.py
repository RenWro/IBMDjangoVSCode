from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    exemplares_disponiveis = models.IntegerField()

    def __str__(self):
        return self.titulo

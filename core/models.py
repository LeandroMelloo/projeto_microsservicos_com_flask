from django.db import models
from recursos.models import Recurso
from comentarios.models import Comentario


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    recursos = models.ManyToManyField(Recurso)
    comentario = models.ManyToManyField(Comentario)
    
    def __str__(self):
        return self.nome

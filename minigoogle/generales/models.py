from django.db import models

class Busqueda(models.Model):
    campo_uno = models.CharField(max_length=100)
    campo_dos = models.IntegerField()
    # Agrega más campos según sea necesario

    def __str__(self):
        return self.campo_uno  # Devuelve un campo representativo del modelo, puede ser campo_uno u otro

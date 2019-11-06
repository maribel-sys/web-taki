from django.db import models

# Create your models here.
class Mercado(models.Model):
    producto = models.CharField(max_length=200)
    class Meta:
        verbose_name = "mercado"
        verbose_name_plural = "mercados"

    def __str__(self):
        return self.producto

class Productos(models.Model):
    producto = models.CharField(max_length=200)
    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.producto

class Recetario(models.Model):
    cantidad = models.CharField(max_length=200)
    producto = models.CharField(max_length=200)

    class Meta:
        verbose_name = "cantidad"
        verbose_name_plural = "cantidades"
        verbose_name = "ingrediente"
        verbose_name_plural = "ingredientes"

    def __str__(self):
        return self.producto
        return self.cantidad


class Recuerdame(models.Model):
    recordatorio = models.CharField(max_length=200)

    class Meta:
        verbose_name = "recordar"
        verbose_name_plural = "recordar"

    def __str__(self):
        return self.recordatorio

        



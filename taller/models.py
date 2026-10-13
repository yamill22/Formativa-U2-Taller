from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=12) 
    direccion = models.TextField()
    edad = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Reparacion(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_ingreso = models.DateField()
    fecha_entrega = models.DateField()
    costo = models.PositiveIntegerField()

    def __str__(self):
        return f"Reparación de {self.cliente.nombre} - {self.descripcion[:20]}..."


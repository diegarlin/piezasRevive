from django.db import models

class Producto(models.Model):

    nombre = models.CharField(max_length=255)

    INTERIOR = 'Interior'
    DIRECCION = 'Direccion'
    EMBRAGUE = 'Embrague'
    MOTOR = 'Motor'
    FRENO = 'Freno'
    ALUMBRADO = 'Alumbrado'
    CARROCERIA = 'Carroceria'

    SEAT = 'Seat'
    AUDI =  'Audi'
    TOYOTA = 'Toyota'
    MINI = 'Mini'
    HONDA = 'Honda'
    Fiat = 'Fiat'

    CATEGORIA = (
        (INTERIOR, 'Interior'),
        (DIRECCION, 'Direccion'),
        (EMBRAGUE,'Embrague'),
        (MOTOR, 'Motor'),
        (FRENO, 'Freno'),
        (ALUMBRADO, 'Alumbrado'),
        (CARROCERIA, 'Carroceria')
    )

    MARCA = (
        (SEAT, 'Seat'),
        (AUDI, 'Audi'),
        (TOYOTA,'Toyota'),
        (MINI, 'Mini'),
        (HONDA, 'Honda'),
        (Fiat, 'Fiat')
    )

    categoria = models.CharField(
        max_length=15,
        choices=CATEGORIA,
        default=INTERIOR,
    )

    marca = models.CharField(
        max_length=10,
        choices=MARCA,
        default=SEAT,
    )

    descripcion = models.TextField()
    precio = models.FloatField()
    #precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.URLField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre + "; Categoria: " + self.categoria


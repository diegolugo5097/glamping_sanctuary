from django.db import models

from core.glamping.models import Glamping

"""
This model will allow me to carry out all the management of the reservations
that are made and that will be sent later.
"""


# Model representing the type identification
class TypeIdentification(models.Model):
    name = models.CharField(verbose_name='Nombre', null=True, max_length=45)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de identificacion'
        ordering = ['id']


# Model representing the company's reserve.
class Booking(models.Model):
    date_entry = models.DateField(verbose_name='Fecha de entrada', null=True, unique=True)
    date_departure = models.DateField(verbose_name='Fecha de salida', null=True, unique=True)
    phone = models.CharField(verbose_name='Telefono', null=True, unique=True, max_length=45)
    email = models.EmailField(verbose_name='Correo electronico', null=True, unique=False, max_length=255)
    glamping = models.ForeignKey(Glamping, verbose_name='Glamping', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.email, self.phone

    class Meta:
        verbose_name = 'Gampling'
        ordering = ['id']

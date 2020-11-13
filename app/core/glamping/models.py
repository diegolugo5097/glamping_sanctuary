from django.db import models
from ckeditor.fields import RichTextField

"""
    These models will allow me the handling and all the management of the
    glamping and the state, once this last one is reserved.
"""


# Model representing options status
class Status(models.Model):
    name = models.CharField(verbose_name='Nombre', max_length=25, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['id']


# Model representing glamping information.
class Glamping(models.Model):
    name = models.CharField(verbose_name='Nombre', null=True, max_length=100)
    description = RichTextField(verbose_name='Descripción', blank=True, null=True)
    quantity_person = models.PositiveIntegerField(verbose_name='Cantidad de persona', null=True)
    status = models.ForeignKey(Status, verbose_name='Estado', null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Imagen', blank=True, null=True)

    def __str__(self):
        return self.name, self.status, self.description

    class Meta:
        verbose_name = 'Glamping',
        verbose_name_plural = 'Glamping'
        ordering = ['id']

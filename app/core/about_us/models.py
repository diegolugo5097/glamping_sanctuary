from django.db import models
from ckeditor.fields import RichTextField


# Model that represents the company's about us
class AboutUs(models.Model):
    title = models.CharField(verbose_name='Titulo', null=True, max_length=255)
    description = RichTextField(verbose_name='Descripción', blank=True, null=True)

    def __str__(self):
        return self.title, self.description

    class Meta:
        verbose_name = 'Acerca de nosotros'
        verbose_name_plural = 'Acerca de nosotros'
        ordering = ['id']

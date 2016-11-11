# coding=utf-8

from django.conf import settings
from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.

class Estado(models.Model):
    iidestado = models.IntegerField('Id Estado', primary_key=True)
    cdescripcion = models.CharField('Estado',
                                    db_column='Descripcion',
                                    max_length=50,
                                    blank=True,
                                    null=True)

    class Meta(object):
        verbose_name_plural = 'Estados'

    def __str__(self):
        return '%s' % self.cdescripcion


class Municipio(models.Model):
    iidestado = models.ForeignKey(Estado)
    iidmunicipio = models.IntegerField('Id Municipio',
                                       db_column='Id Municipio',
                                       blank=False,
                                       null=True)
    cdescripcion = models.CharField('Municipio',
                                    db_column='Descripcion',
                                    max_length=50,
                                    blank=True,
                                    null=True)

    class Meta(object):
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return '%s' % self.cdescripcion


class Ubicacion(models.Model):
    iidubicacion = models.AutoField('Id Ubicación',
                                    primary_key=True)
    iasentamiento = models.IntegerField('Asentamiento',
                                        blank=True,
                                        null=True)
    cdescripcion = models.CharField('Descripción',
                                    db_column='Descripcion',
                                    max_length=80,
                                    blank=True,
                                    null=True)
    icodigopostal = models.IntegerField('Codigo Postal',
                                        db_column='Codigo Postal',
                                        blank=True,
                                        null=True)
    iidmunicipio = models.ForeignKey(Municipio)
    iidestado = models.ForeignKey(Estado)

    class Meta(object):
        verbose_name_plural = 'Ubicaciones'

    def __str__(self):
        return '%s' % self.cdescripcion
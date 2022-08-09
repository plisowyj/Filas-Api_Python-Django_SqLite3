from django.db import models


class UpperCaseCharField(models.CharField):

    def __init__(self, *args, **kwargs):
        super(UpperCaseCharField, self).__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            value = value.upper()
            setattr(model_instance, self.attname, value)
            return value
        else:
            return super(UpperCaseCharField, self).pre_save(model_instance, add)

class Ingresos(models.Model):
    class Meta:
        ordering = ["fec_ingreso"]

    id = models.AutoField(primary_key=True)
    id_tramite = models.IntegerField()
    tram_detalle = models.CharField(max_length=50)
    decorador = models.CharField(max_length=1)
    contador = models.IntegerField()
    id_cliente = models.IntegerField()
    fec_ingreso = models.DateTimeField()
    recibido = models.CharField(max_length=1)
    atendido = models.CharField(max_length=1)
    documento = models.CharField(max_length=11)

class Contadores(models.Model):
    descripcion = models.CharField(max_length=30)
    tipo = models.CharField(max_length=5)
    valor = models.IntegerField()
    fec_ult_actual = models.DateTimeField()

class Anuncios(models.Model):
    class Meta:
        ordering = ["-fec_anuncio"]

    id = models.AutoField(primary_key=True)
    id_ingreso = models.IntegerField()
    fec_anuncio = models.DateTimeField()
    decorador = models.CharField(max_length=1)
    contador = models.IntegerField()
    lugar = models.CharField(max_length=20) 

class Clientes(models.Model):
    id = models.AutoField(primary_key=True)
    apellido = UpperCaseCharField(max_length=50)
    nombres = UpperCaseCharField(max_length=50)
    documento = models.CharField(max_length=11)
    picture = models.ImageField(upload_to="images/",null=True)
    fec_nac = models.DateField(null=True)

class Tramites(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)
    activo = models.CharField(max_length=1)
    decorador = models.CharField(max_length=1)
    lugar = models.CharField(max_length=20)


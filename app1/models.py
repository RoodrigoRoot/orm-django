from django.db import models

# Create your models here.

class ModeloAuditoria(models.Model):
    fecha_crea = models.DateTimeField(auto_now_add=True)
    fecha_modifica = models.DateTimeField(auto_now=True)
    ACTIVO = 'Activo'
    INACTIVO = 'Inactivo'
    ESTADO_OPCIONES = [
        (ACTIVO, 'Activo'),
        (INACTIVO, 'Inctivo'),
        
    ]
    estado = models.CharField(max_length=8, choices=ESTADO_OPCIONES, default=ACTIVO)
    activo = models.BooleanField(default=True)


    class Meta:
        abstract = True


class Categoria(ModeloAuditoria):
    descripcion = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name_plural = "Categorias"

class Persona(ModeloAuditoria):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(blank=False, null=False)

    def __str__(self):
        return "{} {}".format(self.nombre, self.apellido)
    
    def save(self):
        self.nombre = self.nombre.capitalize()
        self.apellido = self.apellido.capitalize()
        super(Persona, self).save()
    
    class Meta:
        verbose_name_plural = "Personas"

class Animal(ModeloAuditoria):
    nombre = models.CharField(max_length=10)
    patas = models.IntegerField(default=2)
    
    def __str__(self):
        return self.nombre

    def save(self):
        self.nombre = self.nombre.upper()
        super(Animal, self).save()


    class Meta:
        verbose_name_plural = "Animales"

class Book(ModeloAuditoria):
    TIPO_OPCIONES=[
        ("Virtual", "Virtual"),
        ("Físico", "Físico")
    ]

    nombre = models.CharField(max_length=50)
    precio_real = models.FloatField(help_text="En Dolares")
    peso = models.PositiveIntegerField(help_text="En Libras")
    tipo = models.CharField(max_length=50, choices=TIPO_OPCIONES)
    url_descarg = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    
    def save(self):
        self.nombre = self.nombre.upper()
        super(Book, self).save()
    
    class Meta:
        verbose_name_plural = "Libros"
        unique_together = ('nombre', 'tipo')

from django.db import models


class Category(models.Model):

    nombre = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(verbose_name='descripcion',max_length=255,blank=True)
    image = models.ImageField(verbose_name='imagen',upload_to='photos/categories/',blank=True)

    class Meta:
        verbose_name = 'CATEGORIA'
        verbose_name_plural = 'Categoria'

    # ME PERMITE QUE ME APARESCA EL NOMBRE,ETC CUANDO LO LLAMO DE OTRA TABLA (FOREIGN KEY)
    def __str__(self):
        return self.nombre


from django.db import models
from category.models import Category

# Create your models here.


class Product(models.Model):

    product_name = models.CharField(verbose_name='nombre',max_length=200,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    description = models.TextField(verbose_name='descripcion',max_length=500,blank=True)
    price = models.IntegerField(verbose_name='precio')
    image = models.ImageField(verbose_name='imagen',upload_to='photos/products')
    stock = models.IntegerField(verbose_name='cantidad')
    is_available = models.BooleanField(verbose_name='disponible?',default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='categoria') 
    created_date = models.DateTimeField(verbose_name='fecha-creacion',auto_now_add=True)
    modified_date = models.DateTimeField(verbose_name='fecha-modificacion',auto_now=True)


     # ME PERMITE QUE ME APARESCA EL NOMBRE,ETC CUANDO LO LLAMO DE OTRA TABLA (FOREIGN KEY)
    def __str__(self):
        return self.product_name

    

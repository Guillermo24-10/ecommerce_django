from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class MyAccountManager(BaseUserManager):

    def  create_user(self, first_name , last_name,username, email , password=None):
        if not email:
            raise ValueError('Debe tener un email')

        if not username:
            raise ValueError('Debe tener un usuario')
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,first_name,last_name,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self.db)
        return user

class Account(AbstractBaseUser):

    
    first_name = models.CharField(verbose_name='nombre',max_length=50)
    last_name = models.CharField(verbose_name='apellido',max_length=50)
    username = models.CharField(verbose_name='usuario',max_length=50,unique=True)
    email = models.EmailField(max_length=100,unique=True)
    phone_number = models.CharField(verbose_name='telefono',max_length=50)
    

    # requerid

    date_joined = models.DateTimeField(verbose_name='fecha_registro',auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(verbose_name='administrador',default=False)
    is_staff = models.BooleanField(verbose_name='personal',default=False)
    is_active = models.BooleanField(verbose_name='activo',default=False)
    is_superadmin = models.BooleanField(verbose_name='super_usuario',default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = MyAccountManager()


    def __str__(self):
        return self.email

    def has_perm(self,perm,obj=None):
        return self.is_admin

    def has_module_perms(self,add_label):
        return True    
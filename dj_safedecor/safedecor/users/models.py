from django.db import models
#from api.models import User
#from django.db.models.signals import post_delete,post_save,pre_save
# Create your models here.
#from safedecor_apps.base.models import TimeStampedModel, GeneratedByModel, Status
from django.utils.translation import ugettext_lazy as _

class Users(models.Model):
    customer_name=models.CharField(max_length=100)
    role = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=40, unique=True)
    password=models.CharField(max_length=15,default="123456")
    
    class Meta:
        managed = True
        verbose_name = _('Users')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.email

class Product_Catalog(models.Model):
    catalog_code = models.CharField(max_length=100,null=True, blank=True)
    catalog_name = models.CharField(max_length=100,null=True, blank=True)
    product_code = models.CharField(max_length=100, null=True, blank=True)
    product_display_code = models.CharField(max_length=100, null=True, blank=True)

    class Meta: 
        managed = True
        verbose_name = _('Product Catalog')
        verbose_name_plural = _('Product Catalog')

    def __str__(self):
        return self.catalog_code

    def __unicode__(self):
        return self.catalog_code

class Distributer_Catalog(models.Model):
    catalog_code = models.CharField(max_length=100,null=True, blank=True)
    distributer_id = models.CharField(max_length=100,null=True, blank=True)
    catalog_name = models.CharField(max_length=100,null=True, blank=True)
    #catalog_image = models.ImageField(upload_to='catalogimage/', null=True, max_length=255)
    catalog_image = models.CharField(max_length=200,null=True, blank=True)
   
    class Meta:
        managed = True
        verbose_name = _('Distributer Catalog')
        verbose_name_plural = _('Distributer Catalog')

    def __str__(self):
        return self.catalog_code

    def __unicode__(self):
        return self.catalog_code


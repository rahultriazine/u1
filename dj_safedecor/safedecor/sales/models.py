from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Sale_to_customers(models.Model):
    distributer_id = models.IntegerField(max_length=20)
    buyer_distributer_id = models.IntegerField(max_length=20,null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField( null=True, blank=True)
    type = models.CharField(max_length=20,null=True, blank=True)
    image = models.ImageField(upload_to='uploadimages/', max_length=250, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now(), null=True, blank=True)
    date_modified = models.DateTimeField(default=timezone.now(), null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = _('Sales')
        verbose_name_plural = _('Sales')

    def __str__(self):
        return self.distributer_id

    def __unicode__(self):
        return self.distributer_id


class Sale_to_customers_detail(models.Model):
    #sales_id = models.ForeignKey(Cliente, related_name="cliente", on_delete=models.PROTECT)
    sales_id = models.ForeignKey(Sale_to_customers, null=True, blank=True, on_delete=models.CASCADE)
    product_id = models.CharField(max_length=100, null=True, blank=True)
    catalog_code = models.CharField(max_length=100, null=True, blank=True)
    qty = models.IntegerField(max_length=20, null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now(), null=True, blank=True)
    date_modified = models.DateTimeField(default=timezone.now(), null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = _('Sales Detail')
        verbose_name_plural = _('Sales Detail')

    def __str__(self):
        return self.catalog_code

    def __unicode__(self):
        return self.catalog_code



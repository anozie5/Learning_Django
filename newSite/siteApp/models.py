from django.db import models

# Create your models here.
class Product (models.Model):
    product_id = models.AutoField(primary_key = True)
    product_name = models.CharField (max_length = 320)
    sku = models.CharField (max_length = 320, unique = True)
    price = models.FloatField()
    quantity = models.IntegerField()
    supplier_name = models.CharField (max_length = 320)

    def __str__(self):
        return self.product_name

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    descriptions = models.TextField()
    price = models.IntegerField()
    company = models.CharField(max_length=20)

    class Meta:
        db_table = 'Product'

    def __str__(self):
        return self.name


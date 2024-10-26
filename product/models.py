from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=155, default="Product name")
    qty = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.title

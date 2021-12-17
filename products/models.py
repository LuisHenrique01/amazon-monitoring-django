import uuid
from django.db import models
from django.contrib.auth.models import User


class UUIDModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class ProductModel(UUIDModel):

    user = models.ManyToManyField(User, related_name='products_user')
    name = models.CharField(max_length=230)
    asin = models.CharField(max_length=10)
    url = models.URLField(max_length=300, default='https://www.amazon.com.br/')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name


class HistoricModel(UUIDModel):

    product = models.ForeignKey(
        ProductModel, on_delete=models.CASCADE, related_name='historic_product')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Historic"
        verbose_name_plural = "Histories"
        ordering = ['-date']

    def __str__(self):
        return self.product.name

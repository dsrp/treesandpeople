from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import (
    NamedBase, CostBase, TaskBase, ProductionBase, CategoryBase
)


class ProductCategory(CategoryBase):
    pass


class Product(NamedBase):
    category = models.ForeignKey(
        ProductCategory, verbose_name=_('category'),
        null=True, on_delete=models.SET_NULL
    )


class ProductBase(models.Model):
    """ Abstract base class for elements relating to Product. """

    class Meta:
        abstract = True

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.product)


class ProductProduction(ProductBase, ProductionBase):
    pass

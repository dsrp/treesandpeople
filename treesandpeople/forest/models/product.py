from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedBase, CostBase, TaskBase, ProductionBase


class ProductType(NamedBase):
    pass


class Product(NamedBase):
    # TODO: This should *NOT* cascade but to be set null instead.
    product_type = models.ForeignKey(ProductType, verbose_name=_('type'), on_delete=models.CASCADE)


class ProductBase(models.Model):
    """ Abstract base class for elements relating to Product. """

    class Meta:
        abstract = True

    poduct = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductCosts(ProductBase, CostBase):
    pass


class ProductTask(ProductBase, TaskBase):
    pass


class ProductProduction(ProductBase, ProductionBase):
    pass

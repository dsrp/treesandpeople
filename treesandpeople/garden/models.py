from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import (
    NamedBase, CostBase, TaskBase, ProductionBase, CategoryBase
)
from culture.models import CultureBase, Culture


class Garden(NamedBase):
    cultures = models.ManyToManyField(Culture, through='GardenCulture')


class GardenBase(models.Model):
    """ Abstract base class for elements relating to garden. """

    class Meta:
        abstract = True

    garden = models.ForeignKey(Garden, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.garden)


class GardenCulture(GardenBase, CultureBase):
    area = models.FloatField(help_text=_('square meter'))


class GardenCostsCategory(CategoryBase):
    class Meta:
        verbose_name = _('cost category')
        verbose_name_plural = _('cost categories')


class GardenCosts(CostBase, GardenBase):
    class Meta:
        verbose_name = _('cost')
        verbose_name_plural = _('costs')

    category = models.ForeignKey(
        GardenCostsCategory, on_delete=models.SET_NULL, null=True
    )


class GardenTaskCategory(CategoryBase):
    pass


class GardenTask(TaskBase, GardenBase):
    category = models.ForeignKey(
        GardenTaskCategory, on_delete=models.SET_NULL, null=True
    )


class GardenProduction(ProductionBase, GardenBase):
    pass

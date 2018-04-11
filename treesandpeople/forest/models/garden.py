from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedBase, CostBase, TaskBase, ProductionBase
from .culture import CultureBase, Culture


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


class GardenCosts(GardenBase, CostBase):
    pass


class GardenTask(GardenBase, TaskBase):
    pass


class GardenProduction(GardenBase, ProductionBase):
    pass

from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedBase, CostBase, TaskBase, ProductionBase


class Species(NamedBase):
    plants_per_area = models.FloatField(
        help_text=_('per square meter')
    )


class SpeciesBase(models.Model):
    """ Abstract base class for elements relating to species. """

    class Meta:
        abstract = True

    species = models.ForeignKey(Species, on_delete=models.CASCADE)


class SpeciesCosts(SpeciesBase, CostBase):
    pass


class SpeciesTask(SpeciesBase, TaskBase):
    pass


class SpeciesProduction(SpeciesBase, ProductionBase):
    pass

from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedBase
from .species import SpeciesBase, Species


class Culture(NamedBase):
    species = models.ManyToManyField(Species, through='CultureSpecies')


class CultureBase(models.Model):
    """ Abstract base class for elements relating to culture. """

    class Meta:
        abstract = True

    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)


class CultureSpecies(CultureBase, SpeciesBase):
    ratio = models.FloatField(
        help_text=_('fraction, monoculture equivalent')
        # TODO: Validate value > 0.0 and <= 1.0
    )

    def __str__(self):
        return self.species.name

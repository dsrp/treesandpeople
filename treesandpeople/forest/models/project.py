from django.db import models
from django.utils.translation import gettext_lazy as _

from .base import NamedBase, CostBase, TaskBase, ProductionBase
from .garden import Garden


class Project(NamedBase):
    gardens = models.ManyToManyField(Garden)

    labour_price = models.FloatField(
        help_text=_('€ per hour')
    )


class ProjectBase(models.Model):
    """ Abstract base class for elements relating to project. """

    class Meta:
        abstract = True

    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class ProjectCosts(ProjectBase, CostBase):
    pass


class ProjectTask(ProjectBase, TaskBase):
    pass


class ProjectProduction(ProjectBase, ProductionBase):
    pass

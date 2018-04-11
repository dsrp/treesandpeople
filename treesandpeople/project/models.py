from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import (
    NamedBase, CostBase, TaskBase, ProductionBase, CategoryBase
)
from garden.models import Garden


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

    def __str__(self):
        return str(self.project)


class ProjectCostsCategory(CategoryBase):
    pass


class ProjectCosts(ProjectBase, CostBase):
    category = models.ForeignKey(
        ProjectCostsCategory, on_delete=models.SET_NULL, null=True
    )


class ProjectTaskCategory(CategoryBase):
    pass


class ProjectTask(ProjectBase, TaskBase):
    category = models.ForeignKey(
        ProjectTaskCategory, on_delete=models.SET_NULL, null=True
    )


class ProjectProduction(ProjectBase, ProductionBase):
    pass

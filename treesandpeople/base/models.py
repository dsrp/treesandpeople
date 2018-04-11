from django.db import models


class NamedBase(models.Model):
    class Meta:
        abstract = True

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class YearBase(models.Model):
    """ Base model for elements relating to a year. """

    class Meta:
        abstract = True

    year = models.IntegerField(db_index=True)


class CostBase(YearBase):
    class Meta:
        abstract = True


class TaskBase(YearBase):
    class Meta:
        abstract = True


class ProductionBase(YearBase):
    class Meta:
        abstract = True

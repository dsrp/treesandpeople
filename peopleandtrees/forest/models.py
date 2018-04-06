from django.db import models


class NamedMixin(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Species(NamedMixin):
    plants_per_area = models.FloatField()


class Culture(NamedMixin):
    species = models.ManyToManyField(Species, through='CultureSpecies')


class CultureSpecies(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    ratio = models.FloatField()


class Forest(NamedMixin):
    pass


class ForestCulture(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    forest = models.ForeignKey(Forest, on_delete=models.CASCADE)

    area = models.FloatField()

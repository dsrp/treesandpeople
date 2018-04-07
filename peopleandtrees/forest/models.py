from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField


class NamedModel(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Product(NamedModel):
    pass


class Species(NamedModel):
    plants_per_area = models.FloatField(
        help_text=_('per square meter')
    )

    # Yearly numbers
    labour_per_plant = ArrayField(models.FloatField(
        help_text=_('hours per year')
    ), size=10)
    costs_per_plant = ArrayField(models.FloatField(
        help_text=_('€ per year, including initial costs')
    ), size=10)

    products = models.ManyToManyField(Product, through='SpeciesProduct')

    def get_plants_per_area(self):
        # TODO: return number of plants per surface area
        pass

    def get_yield_per_area(self):
        # TODO: return yield per surface area, as array, per year
        pass

    def get_costs_per_area(self):
        # TODO: return total costs per surface area, per year
        pass

    def get_gains_per_area(self):
        # TODO: return total gains per surface area, per year
        pass

    def get_labour_per_area(self):
        # TODO: return total labour per surface area, per year
        pass


class SpeciesProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    # Yearly numbers
    yield_per_plant = ArrayField(models.FloatField(
        help_text=_('metric tons per year')
    ), size=10)
    labour_per_plant = ArrayField(models.FloatField(
        help_text=_('hours per year')
    ), size=10)
    costs_per_plant = ArrayField(models.FloatField(
        help_text=_('€ per year')
    ), size=10)

    price = models.FloatField(
        help_text=_('sales price per metric ton')
    )

    def get_yield_per_plant(self):
        # TODO: return yield per surface area, as array, per year
        pass

    def get_costs_per_plant(self):
        # TODO: return total costs per surface area, per year
        pass

    def get_gains_per_plant(self):
        # TODO: return total gains per surface area, per year
        pass

    def get_labour_per_plant(self):
        # TODO: return total labour per surface area, per year
        pass

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')


class Culture(NamedModel):
    species = models.ManyToManyField(Species, through='CultureSpecies')


class CultureSpecies(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    species = models.ForeignKey(Species, on_delete=models.CASCADE)

    ratio = models.FloatField(
        help_text=_('fraction, monoculture equivalent')
        # TODO: Validate value > 0.0 and <= 1.0
    )

    def get_plants_per_area(self):
        # TODO: return number of plants per surface area
        pass


class Forest(NamedModel):
    cultures = models.ManyToManyField(Culture, through='ForestCulture')

    def get_area(self):
        # TODO: Return total area
        pass

    def get_yield(self):
        # TODO: return total yield, as array, per year
        pass

    def get_costs(self):
        # TODO: return total costs, per year
        pass

    def get_gains(self):
        # TODO: return total gains, per year
        pass

    def get_labour(self):
        # TODO
        pass


class ForestCulture(models.Model):
    culture = models.ForeignKey(Culture, on_delete=models.CASCADE)
    forest = models.ForeignKey(Forest, on_delete=models.CASCADE)

    area = models.FloatField()

    def get_area(self):
        # TODO: Return total area
        pass

    def get_yield(self):
        # TODO: return total yield, as array, per year
        pass

    def get_costs(self):
        # TODO: return total costs, per year
        pass

    def get_gains(self):
        # TODO: return total gains, per year
        pass

    def get_labour(self):
        # TODO
        pass


class Project(NamedModel):
    forests = models.ManyToManyField(Forest)

    labour_price = models.FloatField(
        help_text=_('€ per hour')
    )

    def get_area(self):
        # TODO: Return total area
        pass

    def get_yield(self):
        # TODO: return total yield, as array, per year
        pass

    def get_costs(self):
        # TODO: return total costs, per year
        pass

    def get_gains(self):
        # TODO: return total gains, per year
        pass

    def get_labour(self):
        # TODO
        pass

    def get_labour_costs(self):
        # TODO
        pass

    def get_costbenefit(self):
        # TODO: return benefits minus costs, per year
        pass

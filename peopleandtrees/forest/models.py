from django.db import models
from django.utils.translation import gettext_lazy as _


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
        help_text=_('Per square meter.')
    )
    # TODO: array field
    labour_per_plant = models.FloatField(
        help_text=_('Hours of labour per plant, per year.')
    )
    # TODO: array field
    costs_per_plant = models.FloatField(
        help_text=_('In Euros per year, including initial costs.')
    )

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

    # TODO: array field
    yield_per_plant = models.FloatField(
        help_text=_('In metric tons per year.')
    )

    # TODO: array field
    labour_per_plant = models.FloatField(
        help_text=_('In hours per year.')
    )

    # TODO: array field
    costs_per_plant = models.FloatField(
        help_text=_('In Euros per year.')
    )

    price = models.FloatField(
        help_text=_('Sales price per metric ton.')
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
        help_text=_('Fraction of monoculture equivalent for this species.')
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
        help_text=_('Labour price in Euros per hour.')
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

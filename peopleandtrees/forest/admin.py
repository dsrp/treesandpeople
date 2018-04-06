from django.contrib import admin

from .models import (
    Species, SpeciesProduct, Product,
    Culture, CultureSpecies, Forest, ForestCulture
)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


class SpeciesProductInline(admin.TabularInline):
    model = SpeciesProduct


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    inlines = [
        SpeciesProductInline
    ]


class CultureSpeciesInline(admin.TabularInline):
    model = CultureSpecies


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    inlines = [
        CultureSpeciesInline
    ]


class ForestCultureInline(admin.TabularInline):
    model = ForestCulture


@admin.register(Forest)
class ForestAdmin(admin.ModelAdmin):
    inlines = [
        ForestCultureInline
    ]

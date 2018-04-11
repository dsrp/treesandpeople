from django.contrib import admin

from .models import (
    Species, SpeciesProduct, Product,
    Culture, CultureSpecies, Forest, ForestCulture, Project
)


class InlineBase(admin.StackedInline):
    min_num = 0
    # Note: for some reason, extra > 0 gives "This field is required." for all
    # fields of the inline - making it effectively a required value.
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


class SpeciesProductInline(InlineBase):
    model = SpeciesProduct


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    inlines = [
        SpeciesProductInline
    ]


class CultureSpeciesInline(InlineBase):
    model = CultureSpecies


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    inlines = [
        CultureSpeciesInline
    ]


class ForestCultureInline(InlineBase):
    model = ForestCulture


@admin.register(Forest)
class ForestAdmin(admin.ModelAdmin):
    inlines = [
        ForestCultureInline
    ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass

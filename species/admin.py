from django.contrib import admin

from base.admin import InlineBase

from .models import (
    SpeciesCulture, Species,
    SpeciesCostsCategory, SpeciesCosts,
    SpeciesLabourCategory, SpeciesLabour,
    SpeciesProduction
)


class SpeciesCultureInline(InlineBase):
    model = SpeciesCulture


class SpeciesCostsInline(InlineBase):
    model = SpeciesCosts


class SpeciesLabourInline(InlineBase):
    model = SpeciesLabour


class SpeciesProductionInline(InlineBase):
    model = SpeciesProduction


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    inlines = [
        SpeciesCultureInline,
        SpeciesCostsInline,
        SpeciesLabourInline,
        SpeciesProductionInline
    ]


@admin.register(SpeciesCostsCategory)
class SpeciesCostsCategoyAdmin(admin.ModelAdmin):
    pass


@admin.register(SpeciesLabourCategory)
class SpeciesLabourCategoryAdmin(admin.ModelAdmin):
    pass

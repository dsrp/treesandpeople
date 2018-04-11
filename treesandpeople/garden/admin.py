from django.contrib import admin

from base.admin import InlineBase

from .models import (
    GardenCulture, Garden,
    GardenCostsCategory, GardenCosts,
    GardenLabourCategory, GardenLabour,
    GardenProduction
)


class GardenCultureInline(InlineBase):
    model = GardenCulture


class GardenCostsInline(InlineBase):
    model = GardenCosts


class GardenLabourInline(InlineBase):
    model = GardenLabour


class GardenProductionInline(InlineBase):
    model = GardenProduction


@admin.register(Garden)
class GardenAdmin(admin.ModelAdmin):
    inlines = [
        GardenCultureInline,
        GardenCostsInline,
        GardenLabourInline,
        GardenProductionInline
    ]


@admin.register(GardenCostsCategory)
class GardenCostsCategoyAdmin(admin.ModelAdmin):
    pass


@admin.register(GardenLabourCategory)
class GardenLabourCategoryAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

from base.admin import InlineBase

from .models import (
    GardenCulture, Garden,
    GardenCostsCategory, GardenCosts,
    GardenTaskCategory, GardenTask,
    GardenProduction
)


class GardenCultureInline(InlineBase):
    model = GardenCulture


class GardenCostsInline(InlineBase):
    model = GardenCosts


class GardenTaskInline(InlineBase):
    model = GardenTask


class GardenProductionInline(InlineBase):
    model = GardenProduction


@admin.register(Garden)
class GardenAdmin(admin.ModelAdmin):
    inlines = [
        GardenCultureInline,
        GardenCostsInline,
        GardenTaskInline,
        GardenProductionInline
    ]


@admin.register(GardenCostsCategory)
class GardenCostsCategoyAdmin(admin.ModelAdmin):
    pass


@admin.register(GardenTaskCategory)
class GardenTaskCategoryAdmin(admin.ModelAdmin):
    pass

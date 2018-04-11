from django.contrib import admin

from base.admin import InlineBase
from .models import Species, SpeciesProduction


class SpeciesProductionInline(InlineBase):
    model = SpeciesProduction


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    inlines = [
        SpeciesProductionInline
    ]

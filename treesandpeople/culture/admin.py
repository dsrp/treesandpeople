from django.contrib import admin

from base.admin import InlineBase
from .models import Culture, CultureSpecies


class CultureSpeciesInline(InlineBase):
    model = CultureSpecies


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    inlines = [
        CultureSpeciesInline
    ]

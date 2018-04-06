from django.contrib import admin

from .models import Species, Culture, CultureSpecies, Forest, ForestCulture


class CultureSpeciesInline(admin.TabularInline):
    model = CultureSpecies


@admin.register(Species)
class SpeciesAdmin(admin.ModelAdmin):
    pass


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

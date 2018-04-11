from django.contrib import admin

from base.admin import InlineBase
from .models import GardenCulture, Garden


class GardenCultureInline(InlineBase):
    model = GardenCulture


@admin.register(Garden)
class GardenAdmin(admin.ModelAdmin):
    inlines = [
        GardenCultureInline
    ]

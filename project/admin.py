from django.contrib import admin

from base.admin import InlineBase

from .models import (
    Project,
    ProjectCostsCategory, ProjectCosts,
    ProjectLabourCategory, ProjectLabour,
    ProjectProduction
)


class ProjectCostsInline(InlineBase):
    model = ProjectCosts


class ProjectLabourInline(InlineBase):
    model = ProjectLabour


class ProjectProductionInline(InlineBase):
    model = ProjectProduction


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        ProjectCostsInline,
        ProjectLabourInline,
        ProjectProductionInline
    ]


@admin.register(ProjectCostsCategory)
class ProjectCostsCategoyAdmin(admin.ModelAdmin):
    pass


@admin.register(ProjectLabourCategory)
class ProjectLabourCategoryAdmin(admin.ModelAdmin):
    pass

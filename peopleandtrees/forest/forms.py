from django import forms
from django.contrib.postgres.forms import SplitArrayField


def arrayfield():
    return SplitArrayField(forms.FloatField(), size=10)


class SpeciesForm(forms.ModelForm):
    labour_per_plant = arrayfield()
    costs_per_plant = arrayfield()


class SpeciesProductForm(forms.ModelForm):
    yield_per_plant = arrayfield()
    labour_per_plant = arrayfield()
    costs_per_plant = arrayfield()

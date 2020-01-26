from django import forms
from . import models


class RustSourceForm(forms.ModelForm):
    class Meta:
        model = models.RustSource
        fields = ('category',)


class PythonSourceForm(forms.ModelForm):
    class Meta:
        model = models.PythonSource
        fields = ('category',)

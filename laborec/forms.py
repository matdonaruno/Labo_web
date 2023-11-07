from django import forms
from .models import POST

class jikangaiForm(forms.ModelForm):
  class Meta:
    model = POST
    fields = ("recorder", "seika_fridge1", "seika_fridge2", "seika_fridge3", "seika_fridge4", "seika_fridge5", "seika_fridge6", "seika_fridge7", "seika_freezer1")
from django import forms
from main.models import Test


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

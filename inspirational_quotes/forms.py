from django import forms
from .models import InspirationalQuote


class InspirationalQuoteForm(forms.ModelForm):

    class Meta:
        model = InspirationalQuote
        fields = '__all__'

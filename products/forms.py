from django import forms
from .models import Product, Category, Philosopher, Review
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label="Image",
                             required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        philosophers = Philosopher.objects.all()
        p_friendly_names = [
            (p.id, p.get_friendly_name()) for p in philosophers]

        self.fields['philosopher'].choices = p_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = '__all__'

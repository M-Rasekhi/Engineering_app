from django import forms
from .models import Rectangle, FanUnbalance

class RectangleForm(forms.ModelForm):
    class Meta():
        model = Rectangle
        fields = '__all__'

class FanUnbalanceForm(forms.ModelForm):
    class Meta():
        model = FanUnbalance
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['balance_grade'].widget.attrs.update({'class': 'special'})
        self.fields['impeller_mass'].widget.attrs.update({'class': 'special'}, size='200')
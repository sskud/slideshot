from django import forms
from broadcasts.models import Slide, Broadcasting

class SlideForm(forms.ModelForm):
    position = forms.IntegerField(required=False)
    broadcasting = forms.ModelChoiceField(queryset=Broadcasting.objects.all(), required=False)
    class Meta:
        model=Slide
        fields = ['file', 'broadcasting', 'dt_create']
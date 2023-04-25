from django import forms  
from test_model.models import car 

## Create a ModelForm

class carForm(forms.ModelForm):  
    class Meta:  
        model = car
        fields = "__all__"  
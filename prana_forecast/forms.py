from django import forms
from .models import *


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ( 'document',)


class OptionForm(forms.Form):
        OPTIONS = (
                ("Hotlwinter", "Holtwinter"),
                ("Croston", "Croston"),
                ("FbProphet", "FbProphet"),
                )
        selected_method = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=OPTIONS)



class AdvanceForm(forms.Form):
		class Meta:
			model = Advance
			fields = ('hw_param1','hw_param2','hw_param3','c_param1','c_param2' , 'fb_prophet_param1','arima_param1',)
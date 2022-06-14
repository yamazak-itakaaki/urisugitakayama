from django import forms

class HinatazakaFormClass(forms.Form):
    miyozi = forms.CharField()
    name  = forms.CharField()
    birthday= forms.CharField()
    city= forms.CharField()

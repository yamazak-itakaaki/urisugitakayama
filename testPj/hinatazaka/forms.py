from django import forms

class HinatazakaFormClass(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
from django import forms
#(中略)

class KaraokeFormClass(forms.Form):
    Day = forms.CharField()
    people  = forms.CharField()
    test = forms.CharField()
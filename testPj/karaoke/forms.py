from django import forms
#(中略)

class EnqueteForm(forms.Form):
    birth = forms.DateField(
        label='ご利用日',
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        # required=False
        ) 

#表示するための記述
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

      self.fields['day'].widget.attrs['class']='form-control col-11'
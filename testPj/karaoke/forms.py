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


# ログイン
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label#全てのフォームの部品にplaceholderを定義して、入力フォームにフォーム名が表示されるように指定する
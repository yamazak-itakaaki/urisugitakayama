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
from .models import Kaiintouroku

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        # モデルクラスを指定
        model = Kaiintouroku
        fields = ('miyoji','name','address',)
        labels = {'miyoji':"苗字",'name':"名前",'address':"電話番号",}
from django.shortcuts import render

# Create your views here.
from .models import Kaiintouroku
from .models import Yoyaku
from .models import Room
from .forms import EnqueteForm
#(中略)

class EnqueteView(generic.FormView):
    template_name = "karaoke-input.html"
    form_class = EnqueteForm #forms.pyで作ったクラス名
    success_url = reverse_lazy('information:enquete')

# ログイン
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from  .forms import LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin

class Login(LoginView):
    template_name = 'karaoke-login.html'
    form_class = LoginForm
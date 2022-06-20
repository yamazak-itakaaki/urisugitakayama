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
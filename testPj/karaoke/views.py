from django.shortcuts import render
from django.shortcuts import redirect
from .forms import  KaraokeFormClass
# Create your views here.
from .models import Kaiintouroku
from .models import Yoyaku
from .models import Room
#(中略)

def karaokehomeView(request):
    template_name = "karaoke-home.html"

    return render(request,template_name,)

def karaokeinputView(request):
    template_name = "karaoke-input.html"
    form = KaraokeFormClass()
    ctx = {}
    ctx["form"] = form
    if request.POST:
        request.session['Day'] = request.POST['Day']
        request.session['people'] = request.POST['people']
        return redirect('karaoke-room')
    return render(request, template_name,ctx) 

def karaokeroomView(request):
    template_name = "karaoke-room.html"
    form = KaraokeFormClass()
    ctx = {}
    ctx["form"] = form
    if request.POST:
        judge = request.POST['test']
        if judge == '1':
            request.session['room_id'] = '1' # 4人部屋
            request.session['time'] = '10' # 時間
            return redirect('karaoke-time', '1')
    return render(request, template_name, ctx)

def karaokenetimeView(request, number):
    template_name = "karaoke-time.html"
    ctx = {}
    ctx['time'] = request.session['time']
    return render(request, template_name, ctx) 




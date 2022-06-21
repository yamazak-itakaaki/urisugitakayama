from django.shortcuts import render

# Create your views here.
from .models import Kaiintouroku
from .models import Yoyaku
from .models import Room
#(中略)

def karaokehomeView(request):
    template_name = "karaoke-home.html"

    return render(request,template_name,)

def karaokeinputView(request,id):
    template_name = "karaoke-input.html"
    ctx = {}
    q = Hinatazaka46.objects.get(id=id)
    ctx["object"] = q

    return render(request, template_name,ctx) 

def karaokeroomView(request):
    template_name = "karaoke-room.html"
    if request.POST:
        request.session['time'] = number
        return redirect('hinatazaka-list')
    return render(request, template_name, ctx)

def karaokenetimeView(request, number):
    template_name = "karaoke-time.html"
    request.session['time'] = number
    ctx = {}
    ctx['time'] = request.session['time']
    return render(request, template_name, ctx) 




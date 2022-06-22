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
def karaokehomeView(request):
    template_name = "karaoke-home.html"

    return render(request,template_name,)

def karaokeinputView(request,id):
    template_name = "karaoke-input.html"
    ctx = {}
    q = Hinatazaka46.objects.get(id=id)
    ctx["object"] = q

    return render(request, template_name,ctx)

def karaokeloginView(request):
    template_name="karaoke-login.html"
    form = HinatazakaFormClass()
    ctx = {}
    ctx["form"] = form
    if request.POST:
        miyozi = request.POST["miyozi"]
        name = request.POST["name"]
        birthday = request.POST["birthday"]
        city = request.POST["city"]
        obj = Hinatazaka46(miyozi=miyozi,name=name,birthday=birthday,city=city)
        obj.save()
        return redirect('hinatazaka-list')
    
    return render(request, template_name, ctx)


def karaokenewmemberView(request, id):
    template_name = "karaoke-newmember.html"
    obj = get_object_or_404(Hinatazaka46, id=id)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
        return redirect("hinatazaka-list")
    return render(request, template_name, ctx)

    from .forms import  HinatazakaFormClass


def karaokenewmembercheckView(request, id):
    template_name = "karaoke-newmemberCheck.html"
    obj = get_object_or_404(Hinatazaka46, id=id)
    initial_values = {"miyozi":obj.miyozi,"name":obj.name,"birthday":obj.birthday,"city":obj.city}
    form = HinatazakaFormClass(request.POST or initial_values)
    ctx = {"form": form}
    ctx["obj"] = obj
    if form.is_valid():
        miyozi = form.cleaned_data["miyozi"]
        name = form.cleaned_data["name"]
        birthday = form.cleaned_data["birthday"]
        city = form.cleaned_data["city"]
        obj.miyozi = miyozi
        obj.name = name
        obj.birthday = birthday
        obj.city = city
        obj.save()
        if request.POST:
            return redirect('hinatazaka-list')
    return render(request, template_name, ctx) 

def karaokeroomView(request):
    template_name = "karaoke-room.html"
    if request.POST:
        request.session['time'] = number
        return redirect('hinatazaka-list')
    return render(request, template_name, ctx)

def karaokenetimeView(request, number):
    template_name = "karaoke-time.html"
    request.session['time'] = number
    ctx['time'] = request.session['time']
    return render(request, template_name, ctx) 



        return render(request,"App_Folder_HTML/register.html",context=self.params)



from django.shortcuts import render
from .models import Hinatazaka46

from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404

# Create your views here.
def hinatazakaListView(request):
    template_name = "hinatazaka-list.html"
    ctx = {}
    qs = Hinatazaka46.objects.all()
    ctx["object_list"] = qs
    return render(request,template_name, ctx)

def hinatazakaProfileView(request,id):
    template_name = "hinatazaka-profile.html"
    ctx = {}
    q = Hinatazaka46.objects.get(id=id)
    ctx["object"] = q

    return render(request, template_name,ctx)

def hinatazakaCreateView(request):
    template_name="hinatazaka-form.html"
    if request.POST:
        miyozi = request.POST["miyozi"]
        name = request.POST["name"]
        birthday = request.POST["birthday"]
        city = request.POST["city"]
        obj = Hinatazaka46(miyozi=miyozi,name=name,birthday=birthday,city=city)
        obj.save()
        return redirect('hinatazaka-list')
    
    return render(request, template_name)


def hinatazakaDeleteView(request, id):
    template_name = "hinatazaka-delete.html"
    obj = get_object_or_404(Hinatazaka46, id=id)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
        return redirect('hinatazaka-list')
    return render(request, template_name, ctx)
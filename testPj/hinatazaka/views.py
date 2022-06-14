from django.shortcuts import render
from .models import Hinatazaka46
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

def nippoCreateView(request):
    template_name="hinatazaka-form.html"
    if request.POST:
        miyozi = request.POST["miyozi"]
        name = request.POST["name"]
        brithday = request.POST["brithday"]
        city = request.POST["city"]
    
    return render(request, template_name)

def nippoDeleteView(request, pk):
    template_name = "hinatazaka-delete.html"
    obj = get_object_or_404(Hinatazaka46, pk=pk)
    ctx = {"object": obj}
    return render(request, template_name, ctx)

def nippoDeleteView(request, pk):
    template_name = "hinatazaka-delete.html"
    obj = get_object_or_404(Hinatazaka46, pk=pk)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
    return render(request, template_name, ctx)
from django.shortcuts import render
from .models import Hinatazaka46
# Create your views here.
def hinatazakaListView(request):
    template_name = "hinatazaka-list.html"
    ctx = {}
    qs = Hinatazaka46.objects.all()
    ctx["object_list"] = qs
    return render(request,template_name, ctx)

def hinatazakaProfileView(request,pk):
    template_name = "hinatazaka-profile.html"
    ctx = {}
    q = Hinatazaka46.objects.get(pk=pk)
    ctx["object"] = q
    return render(request, template_name,ctx)
from django.shortcuts import render
from .models import Hinatazaka46
from django.shortcuts import redirect
from .forms import  HinatazakaFormClass
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


def hinatazakaDeleteView(request, id):
    template_name = "hinatazaka-delete.html"
    obj = get_object_or_404(Hinatazaka46, id=id)
    ctx = {"object": obj}
    if request.POST:
        obj.delete()
        return redirect("hinatazaka-list")
    return render(request, template_name, ctx)

    from .forms import  NippoFormClass


# def hinatazakaUpdateFormView(request, id):
#     template_name = "hinatazaka-form.html"
#     obj = Hinatazaka46.objects.get(id=id)
#     initial_values = {"miyozi":obj.miyozi,"name":obj.name,"birthday":obj.birthday,"city":obj.city}
#     form = HinatazakaFormClass(request.POST or initial_values)
#     ctx = {"form": form}
#     if form.is_valid():
#         miyozi = form.cleaned_data["miyozi"]
#         name = form.cleaned_data["name"]
#         birthday = form.cleaned_data["birthday"]
#         city = form.cleaned_data["city"]
#         obj.miyozi = miyozi
#         obj.name = name
#         obj.birthday = birthday
#         obj.city = city
#         obj.save()
#         return redirect('hinatazaka-list')
#     return render(request, template_name, ctx) 

def hinatazakaEditFormView(request, id):
    template_name = "formclass.html"
    #idをもとにユーザ情報を取得
    obj = Hinatazaka46.objects.get(id=id)
    #フォームをオブジェクトを作成
    userForm = UserForm(instance=obj)
    
    #ユーザ情報をフォームに格納
    context = {
        'obj':obj,
        'userForm':userForm,
    }
 
    #user.htmlへデータを渡す
    return render(request, template_name, context)

def hinatazakaUpdateFormView(request,id):
    #リクエストがPOSTの場合
    if request.method == 'POST':
        #idからユーザデータを取得
        obj = Hinatazaka46.objects.get(id=id)
        #ユーザ情報と、リクエストをもとにフォームをインスタンス化
        userForm = UserForm(request.POST,instance=obj)
        if userForm.is_valid():
            userForm.save()
 
    #更新後、対象ユーザの情報を表示
    # obj = Hinatazaka46.objects.get(id=id)
    # context = {
    #     'userinfoDetail': obj,
    # }
 
    #detail.htmlへデータを渡す
    return render(request, 'hinatazaka-list.html',context)

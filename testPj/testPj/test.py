# ここでは、「test.pyファイルが実行されたら、『test.html』を開いてください！」といった内容のコードを書いています。
from django.shortcuts import render
 
def test(request):
    return render(request, 'test.html')
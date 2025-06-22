from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Member

# Create your views here.
def signup_page(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    else:
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        name = request.POST.get('name')
        nicname = request.POST.get('nicname')
        print("id = ", id)
        print("pw = " + pw)
        print("name = " + name)
        print("nicname = " + nicname)
        return JsonResponse({"success":False, "error":"테스트 중입니다."})

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        # 로그인 검증 로직
        print("로그인")
        return redirect('/BapGo/start/')
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

        if Member.objects.filter(id = id).exists():# select id from Member where id = id;
            return JsonResponse({"success":False, "error":"이미 존재하는 아이디입니다."})
        
        Member.objects.create(id=id, pw=pw, name=name, nicname=nicname)

        request.session['user_id'] = id

        return JsonResponse({"success":True, "error":"회원가입 되었습니다."})

def login(request):
    if request.method == "GET":
        if request.session.get('user_id'):
            return redirect('/BapGo/start/')
        return render(request, 'login.html')
    else:
        # 로그인 검증 로직
        id = request.POST.get('userName')
        pw = request.POST.get('userPassword')

        user = Member.objects.filter(id=id, pw=pw).first()
        if user:
            request.session['user_id'] = id
            return redirect('/BapGo/start/')    
        else:
            return render(request, 'login.html', {'error_message':"아이디 또는 비밀번호가 일치하지 않습니다."})
        
def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')
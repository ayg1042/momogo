from django.shortcuts import render
from momogo.settings import KAKAO_API_KEY

def start(request):
    context = {
        'kakao_api_key': KAKAO_API_KEY
    }
    return render(request, 'start.html', context)

def invite(request):
    return render(request, 'invite.html')
from django.shortcuts import render
from django.http import JsonResponse

import roomDetail
# from .models import KAKAO_API_TE, GOOGLE_API_TE
# from .google_api import GooglePlace
from momogo.settings import KAKAO_API_KEY
from datetime import datetime

# Create your views here.
def login(request):
    return render(request, 'login.html')



def room_page(request):
    return render(request, 'room.html')


def create_room(request):    
    print("들어온겨?")
    user = request.user  # 로그인된 사용자
    print(user)

    # TODO: 검색어, 장소 정보 활용해서 room 추가
    
    
    """ 
    Member.objects.create(id=id, pw=pw, name=name, nicname=nicname)

    room = room.objects.create(
        
        )  # 방 생성
    roomDetail.objects.create(
        room_id=room.id,
        user_id=user.member,
        user_status=0  # 방장
    ) 
    """
    
    return JsonResponse({ 'room_id': 0 })
    # return JsonResponse({})
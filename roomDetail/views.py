from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def login(request):
    return render(request, 'login.html')



def add_members(request):
    # TODO: 사용자 정보 활용해서 room id에 연결 추가
    room_id = request.POST.get('room_id')
    user_ids = request.POST.getlist('ids[]')

    count = 0

    return JsonResponse({ "invited_count": count })
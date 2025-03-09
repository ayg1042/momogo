import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import KAKAO_API_TE

from django.shortcuts import render
from momogo.settings import KAKAO_API_KEY

def start(request):
    context = {
        'kakao_api_key': KAKAO_API_KEY
    }
    return render(request, 'start.html', context)

@csrf_exempt  # CSRF 검증 비활성화 (테스트용)
def save_kakao_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            places = data.get("places", [])

            for item in places:
                KAKAO_API_TE.objects.update_or_create(
                    kakao_id=item["id"],
                    defaults={
                        "place_name": item["place_name"],
                        "road_address_name": item.get("road_address_name", ""),
                        "latitude": float(item["y"]),
                        "longitude": float(item["x"]),
                    }
                )

            return JsonResponse({"message": "데이터 저장 완료!"}, status=201)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "POST 요청만 허용됩니다."}, status=405)

def invite(request):
    return render(request, 'invite.html')